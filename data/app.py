from flask import Flask,request,jsonify,Response,make_response
import pickle
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
import scipy.stats as ss
import os
import logging
from flask_cors import CORS

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
dbPath = os.path.join(APP_ROOT, "./model/db_model.sav")
hdPath = os.path.join(APP_ROOT, "./model/hd_model.sav")
dbScorePath = os.path.join(APP_ROOT, "./model/db_score.sav")
hdScorePath = os.path.join(APP_ROOT, "./model/hd_score.sav")
db = pickle.load(open(dbPath, "rb"))
hd = pickle.load(open(hdPath, "rb"))
db_scores = pickle.load(open(dbScorePath, "rb"))
hd_scores = pickle.load(open(hdScorePath, "rb"))

app = Flask(__name__)
cors = CORS(app, resources={r"/update/*": {"origins": "*"}})

@app.route('/predict/', methods=['POST'])
def predict():
    target = request.args.get('target')
    data = request.get_json()
    df = pd.DataFrame([data])
    change = 0
    if(target == 'db'):
        result = db.predict(df)[-1]
        app.logger.info(result)
        return str(result)
    elif(target == 'hd'):
        result = hd.predict(df)[-1]
        return str(result)
    return jsonify({"status": 100, "message": "Input params is diabete or heart."})

@app.route('/update/', methods=['POST'])	
def update():
    global db_scores, hd_scores
    change = 0
    f = request.files['file']
    data=pd.read_csv(f)
    if(sorted(data.columns.tolist()) != sorted(['diabetes', 'heart', 'fbs', 'bmi', 'waist', 'age', 'bpsy', 'bpdi', 'tchol', 'hdl', 'dbfam'])):
        return Response(status=400)
    norm = data[data['heart']==0]
    disease = data[data['heart']==1]
    z_scores = ss.zscore(norm[['fbs','bmi','waist','tchol','hdl','bpdi','bpsy']])
    abs_z_scores = np.abs(z_scores)
    filtered_entries = (abs_z_scores < 3).all(axis=1)
    norm = norm[filtered_entries].sample(n=2*(disease.shape[0]))
    z_scores = ss.zscore(disease[['fbs','bmi','waist','tchol','hdl','bpdi','bpsy']])
    abs_z_scores = np.abs(z_scores)
    filtered_entries = (abs_z_scores < 3).all(axis=1)
    disease = disease[filtered_entries]
    hdata = norm.append(disease).sort_index().reset_index().drop(['index','bmi','diabetes'],axis=1)

    norm = data[data['diabetes']==0]
    disease = data[data['diabetes']==1]
    z_scores = ss.zscore(norm[['fbs','bmi','waist','tchol','hdl','bpsy']])
    abs_z_scores = np.abs(z_scores)
    filtered_entries = (abs_z_scores < 3).all(axis=1)
    norm = norm[filtered_entries].sample(n=2*(disease.shape[0]))
    z_scores = ss.zscore(disease[['fbs','bmi','waist','tchol','hdl','bpsy']])
    abs_z_scores = np.abs(z_scores)
    filtered_entries = (abs_z_scores < 3).all(axis=1)
    disease = disease[filtered_entries]
    ddata = norm.append(disease).sort_index().reset_index().drop(['index','bpdi','heart'],axis=1)

    db_y = ddata.diabetes
    db_x = ddata.drop('diabetes',axis=1)
    clf = tree.DecisionTreeClassifier(max_depth=5)
    x_train, x_test, y_train, y_test = train_test_split(db_x, db_y, test_size=0.3)
    dbtree = clf.fit(x_train, y_train)
    y_scores = dbtree.predict(x_test)
    dbtree_scores = [f1_score(y_test, y_scores),accuracy_score(y_test, y_scores)]
    if all(dbtree_scores[i] >= db_scores[i] for i in range(len(db_scores))) :
        db_scores = dbtree_scores
        dbmodel = dbtree

    hd_y = hdata.heart
    hd_x = hdata.drop('heart',axis=1)
    clf = tree.DecisionTreeClassifier(max_depth=5)
    x_train, x_test, y_train, y_test = train_test_split(hd_x, hd_y, test_size=0.3)
    hdtree = clf.fit(x_train, y_train)
    y_scores = hdtree.predict(x_test)
    hdtree_scores = [f1_score(y_test, y_scores),accuracy_score(y_test, y_scores)]
    if all(hdtree_scores[i] >= hd_scores[i] for i in range(len(hd_scores))) :
        hd_scores = hdtree_scores
        hdmodel = hdtree

    clf = RandomForestClassifier(max_depth=7)
    x_train, x_test, y_train, y_test = train_test_split(db_x, db_y, test_size=0.3)
    dbforest = clf.fit(x_train, y_train)
    y_scores = dbforest.predict(x_test)
    dbforest_scores = [f1_score(y_test, y_scores),accuracy_score(y_test, y_scores)]
    if all(dbforest_scores[i] >= db_scores[i] for i in range(len(db_scores))) :
        db_scores = dbforest_scores
        dbmodel = dbforest

    clf = RandomForestClassifier(max_depth=7)
    x_train, x_test, y_train, y_test = train_test_split(hd_x, hd_y, test_size=0.3)
    hdforest = clf.fit(x_train, y_train)
    y_scores = hdforest.predict(x_test)
    hdforest_scores = [f1_score(y_test, y_scores),accuracy_score(y_test, y_scores)]
    if all(hdforest_scores[i] >= hd_scores[i] for i in range(len(hd_scores))) :
        hd_scores = hdforest_scores
        hdmodel = hdforest

    clf = MLPClassifier(solver='adam', hidden_layer_sizes=(16, 16, 8),max_iter=500)
    x_train, x_test, y_train, y_test = train_test_split(db_x, db_y, test_size=0.3)
    dbmlp = clf.fit(x_train, y_train)
    y_scores = dbmlp.predict(x_test)
    dbmlp_scores = [f1_score(y_test, y_scores),accuracy_score(y_test, y_scores)]
    if all(dbmlp_scores[i] >= db_scores[i] for i in range(len(db_scores))) :
        db_scores = dbmlp_scores
        dbmodel = dbmlp

    clf = MLPClassifier(solver='adam', hidden_layer_sizes=(16, 16, 8),max_iter=500)
    x_train, x_test, y_train, y_test = train_test_split(hd_x, hd_y, test_size=0.3)
    hdmlp = clf.fit(x_train, y_train)
    y_scores = hdmlp.predict(x_test)
    hdmlp_scores = [f1_score(y_test, y_scores),accuracy_score(y_test, y_scores)]
    if all(hdmlp_scores[i] >= hd_scores[i] for i in range(len(hd_scores))) :
        hd_scores = hdmlp_scores
        hdmodel = hdmlp
    
    if 'hdmodel' in locals():
        global hd
        pickle.dump(hdmodel, open('model/hd_model.sav', 'wb'))
        hd = pickle.load(open(hdPath,'rb'))
        pickle.dump(hd_scores, open('model/hd_score.sav', 'wb'))
        hd_scores = pickle.load(open(hdScorePath,'rb'))
        change = 1

    if 'dbmodel' in locals():
        global db
        pickle.dump(dbmodel, open('model/db_model.sav', 'wb'))
        db = pickle.load(open(dbPath,'rb'))
        pickle.dump(db_scores, open('model/db_score.sav', 'wb'))
        hd_scores = pickle.load(open(hdScorePath,'rb'))
        change = 1

    if change:
        res = make_response(jsonify({"message": "อัพเดทโมเดลสำเร็จ"}),200,)
        return res
    res = make_response(jsonify({"message": "โมเดลเดิมมีประสิทธิภาพที่ดีกว่าหรือใกล้เคียงกัน"}),200,)
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)