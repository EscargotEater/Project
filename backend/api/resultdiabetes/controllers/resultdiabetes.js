"use strict";

/**
 * Read the documentation (https://strapi.io/documentation/developer-docs/latest/development/backend-customization.html#core-controllers)
 * to customize this controller
 */

const axios = require("axios");

module.exports = {
  async findID(ctx) {
    const user = ctx.state.user;
    const { date_from, date_to } = ctx.request.body;
    if (user) {
      const res = await strapi.query("resultdiabetes").find({
        userID: user.id,
        created_at_gte: new Date(date_from),
        created_at_lte: new Date(date_to),
      });
      ctx.send(res);
    }
  },
  async predict(ctx) {
    const { fbs, waist, age, bpsy, tchol, hdl, weight, height, dbfam } =
      ctx.request.body;
    const user = ctx.state.user;
    const bmi = (weight / ((height / 100) * (height / 100))).toFixed(2);
    const result = await axios.post(
      "http://localhost:5000/predict/?target=db",
      {
        fbs,
        bmi,
        waist,
        age,
        bpsy,
        tchol,
        hdl,
        dbfam,
      }
    );
    const risk_db = parseInt(result.data);
    console.log(risk_db);
    if (user) {
      const id = user.id;
      const res = await strapi.query("resultdiabetes").create({
        userID: id,
        age,
        bmi,
        bpsy,
        fbs,
        tchol,
        hdl,
        height,
        weight,
        risk_db,
        waist,
        dbfam,
      });
    }
    ctx.send(risk_db);
  },
};
