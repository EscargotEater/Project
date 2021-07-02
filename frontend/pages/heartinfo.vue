<template>
  <b-container class="my-5">
    <b-row>
      <b-col cols="12">
        <p class="b">ข้อมูลโรคหัวใจ</p>
        <hr class="my-4" />
        <p class="p">โรคหัวใจคืออะไร?</p>
        <p class="q">
          คือโรคต่าง ๆ ที่ส่งผลกระทบต่อการทำงานของหัวใจ
          ซึ่งสามารถแบ่งย่อยได้เป็นหลายกลุ่มโรค ดังนี้
        </p>

        <b-img src="~assets/44.jpg" fluid center alt="Responsive image" />

        <p class="p">อาการของโรคหัวใจ</p>
        <p class="q">
          มีทั้งหมด 5 ชนิด ได้แก่ โรคหลอดเลือดหัวใจ โรคกล้ามเนื้อหัวใจ
          โรคลิ้นหัวใจ โรคหัวใจเต้นผิดจังหวะ และโรคติดเชื้อที่เยื่อบุหัวใจ
        </p>

        <b-navbar toggleable type="light">
          <b-navbar-brand href="#"
            ><p class="r">1. อาการของโรคหลอดเลือดหัวใจ</p></b-navbar-brand
          >
          <b-navbar-toggle target="navbar-toggle-collapse" class="s">
            <template #default="{ expanded }">
              <b-icon
                v-if="expanded"
                icon="chevron-bar-up"
                font-scale="1.5"
              ></b-icon>
              <b-icon v-else icon="chevron-bar-down" font-scale="1"></b-icon>
            </template>
          </b-navbar-toggle>
          <b-collapse id="navbar-toggle-collapse" is-nav>
            <b-navbar-nav class="u">
              <b-nav-item>
                <p class="t" style="text-indent: 70px; margin-top: 10px">
                  เกิดจากหลอดเลือดหัวใจตีบจะส่งผลให้เลือดไม่สามารถไปเลี้ยงหัวใจได้เพียงพอ
                  ซึ่งจะส่งผลให้มีอาการเจ็บหน้าอก ใจสั่น หน้ามืด หรือหมดสติ
                </p>
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>

        <b-navbar toggleable type="light">
          <b-navbar-brand href="#"
            ><p class="r">2. อาการของโรคหัวใจเต้นผิดจังหวะ</p></b-navbar-brand
          >
          <b-navbar-toggle target="navbar-toggle-collapse1" class="s">
            <template #default="{ expanded }">
              <b-icon
                v-if="expanded"
                icon="chevron-bar-up"
                font-scale="1.5"
              ></b-icon>
              <b-icon v-else icon="chevron-bar-down" font-scale="1"></b-icon>
            </template>
          </b-navbar-toggle>
          <b-collapse id="navbar-toggle-collapse1" is-nav>
            <b-navbar-nav class="u">
              <b-nav-item>
                <p class="t" style="text-indent: 70px; margin-top: 10px">
                  ผู้ป่วยจะมีอาการ หัวใจเต้นเร็วหรือช้าผิดปกติ
                  เจ็บหน้าอกหรือรู้สึกไม่ค่อยสบาย เวียนศีรษะ มึนงง หรือหมดสติ
                </p>
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>

        <b-navbar toggleable type="light">
          <b-navbar-brand href="#"
            ><p class="r">3. อาการของโรคกล้ามเนื้อหัวใจ</p></b-navbar-brand
          >
          <b-navbar-toggle target="navbar-toggle-collapse2" class="s">
            <template #default="{ expanded }">
              <b-icon
                v-if="expanded"
                icon="chevron-bar-up"
                font-scale="1.5"
              ></b-icon>
              <b-icon v-else icon="chevron-bar-down" font-scale="1"></b-icon>
            </template>
          </b-navbar-toggle>
          <b-collapse id="navbar-toggle-collapse2" is-nav>
            <b-navbar-nav class="u">
              <b-nav-item>
                <p class="t" style="text-indent: 70px; margin-top: 10px">
                  ผู้ที่เป็นจะมีอาการ หายใจไม่อิ่มเมื่อต้องออกแรง ขา เท้า
                  หรือข้อเท้าบวม เหนื่อยล้า วิงเวียนศีรษะ คล้ายจะเป็นลม หรือ
                  เจ็บหน้าอก
                </p>
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>

        <b-navbar toggleable type="light">
          <b-navbar-brand href="#"
            ><p class="r">4. อาการของโรคลิ้นหัวใจ</p></b-navbar-brand
          >
          <b-navbar-toggle target="navbar-toggle-collapse4" class="s">
            <template #default="{ expanded }">
              <b-icon
                v-if="expanded"
                icon="chevron-bar-up"
                font-scale="1.5"
              ></b-icon>
              <b-icon v-else icon="chevron-bar-down" font-scale="1"></b-icon>
            </template>
          </b-navbar-toggle>
          <b-collapse id="navbar-toggle-collapse4" is-nav>
            <b-navbar-nav class="u">
              <b-nav-item>
                <p class="t">
                  ผู้ที่เป็นจะ มีไข้ อ่อนเพลียหรือเหนื่อยล้า ไอแห้ง ๆ
                  อย่างต่อเนื่องเป็นเวลานาน มีผื่นหรือจุดผิดปกติขึ้นบนผิวหนัง
                  หรือ อาการบวมที่ขาหรือช่องท้อง
                </p>
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>

        <p class="p">สาเหตุของโรคหัวใจ</p>
        <p class="q">โรคหัวใจแต่ละชนิดมีสาเหตุดังนี้</p>
        <b-navbar toggleable type="light">
          <b-navbar-brand href="#"
            ><p class="r">1. สาเหตุของโรคหลอดเลือดหัวใจ</p></b-navbar-brand
          >
          <b-navbar-toggle target="navbar-toggle-collapse5" class="s">
            <template #default="{ expanded }">
              <b-icon
                v-if="expanded"
                icon="chevron-bar-up"
                font-scale="1.5"
              ></b-icon>
              <b-icon v-else icon="chevron-bar-down" font-scale="1"></b-icon>
            </template>
          </b-navbar-toggle>
          <b-collapse id="navbar-toggle-collapse5" is-nav>
            <b-navbar-nav class="u">
              <b-nav-item>
                <p class="t" style="text-indent: 70px; margin-top: 10px">
                  โรคหลอดเลือดหัวใจหมายถึงความบกพร่องของหลอดเลือดหัวใจ
                  ส่วนมากมักใช้เรียกภาวะหลอดเลือดแดงตีบ
                </p>
                <p class="t" style="text-indent: 70px">
                  ภาวะหลอดเลือดแดงตีบเกิดจากการสะสมของไขมันในหลอดเลือดแดงที่เพิ่มมากขึ้นเรื่อย
                  ๆ จนผนังของหลอดเลือดหนาและแข็งตัว ทำให้อวัยวะและเนื้อเยื่อต่าง
                  ๆ
                  ที่เชื่อมต่อกับหลอดเลือดแดงดังกล่าวได้รับเลือดไปหล่อเลี้ยงไม่เพียงพอ
                  และเกิดภาวะกล้ามเนื้อหัวใจขาดเลือดเฉียบพลัน
                </p>
                <p class="t" style="text-indent: 70px">
                  ซึ่งโรคนี้จะเกิดในผู้ที่มีอายุมาก มีความดันโลหิตสูง
                  คอเลสเตอรอลสูง ผู้ป่วยเบาหวาน และผู้ป่วยโรคอ้วน
                </p>
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>

        <b-navbar toggleable type="light">
          <b-navbar-brand href="#"
            ><p class="r">2. สาเหตุของโรคหัวใจเต้นผิดจังหวะ</p></b-navbar-brand
          >
          <b-navbar-toggle target="navbar-toggle-collapse6" class="s">
            <template #default="{ expanded }">
              <b-icon
                v-if="expanded"
                icon="chevron-bar-up"
                font-scale="1.5"
              ></b-icon>
              <b-icon v-else icon="chevron-bar-down" font-scale="1"></b-icon>
            </template>
          </b-navbar-toggle>
          <b-collapse id="navbar-toggle-collapse6" is-nav>
            <b-navbar-nav class="u">
              <b-nav-item>
                <p class="t" style="text-indent: 70px; margin-top: 10px">
                  ผู้ที่เป็นโรคนี้อาจะมีสาเหตุมาจาก มีความดันโลหิตสูง สูบบุหรี่
                  ดื่มแอลกอฮอล์หรือเครื่องดื่มที่มีคาเฟอีนมากเกินไป และ เครียด
                  เป็นต้น
                </p>
                >
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>

        <b-navbar toggleable type="light">
          <b-navbar-brand href="#"
            ><p class="r">3. สาเหตุของโรคกล้ามเนื้อหัวใจ</p></b-navbar-brand
          >
          <b-navbar-toggle target="navbar-toggle-collapse7" class="s">
            <template #default="{ expanded }">
              <b-icon
                v-if="expanded"
                icon="chevron-bar-up"
                font-scale="1.5"
              ></b-icon>
              <b-icon v-else icon="chevron-bar-down" font-scale="1"></b-icon>
            </template>
          </b-navbar-toggle>
          <b-collapse id="navbar-toggle-collapse7" is-nav>
            <b-navbar-nav class="u">
              <b-nav-item>
                <p class="t" style="margin-top: 10px">
                  ขึ้นอยู่กับโรคกล้ามเนื้อหัวใจแต่ละชนิด
                </p>
                <p class="v">
                  - โรคกล้ามเนื้อหัวใจเสื่อม
                  เป็นผลจากการไหลเวียนของเลือดไปสู่หัวใจที่ลดน้อยลง การติดเชื้อ
                  การได้รับสารพิษหรือยาบางชนิด รวมถึงการได้รับพันธุกรรมถ่ายทอด
                </p>
                <p class="v">
                  - โรคกล้ามเนื้อหัวใจหนา ผู้ป่วยมักมีกล้ามเนื้อหัวใจหนาผิดปกติ
                  โดยมักเป็นผลจากการถ่ายทอดทางพันธุกรรม
                  หรือเกิดการพัฒนาของโรคไปตามเวลา
                  เนื่องจากอายุที่มากขึ้นหรือความดันโลหิตที่สูงขึ้น
                </p>
                <p class="v">
                  - โรคกล้ามเนื้อหัวใจถูกบีบรัด
                  ภาวะกล้ามเนื้อหัวใจที่แข็งและยืดหยุ่นน้อยลง
                  ซึ่งอาจเกิดขึ้นได้โดยไม่ทราบสาเหตุ
                  หรือเป็นผลจากการป่วยเป็นโรคอื่น ๆ เช่น
                  โรคเนื้อเยื่อเกี่ยวพันผิดปกติ
                  ภาวะที่ร่างกายสร้างหรือรับธาตุเหล็กมากเกิน หรือ การทำเคมีบำบัด
                </p>
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>

        <b-navbar toggleable type="light">
          <b-navbar-brand href="#"
            ><p class="r">4. สาเหตุของโรคติดเชื้อบริเวณหัวใจ</p></b-navbar-brand
          >
          <b-navbar-toggle target="navbar-toggle-collapse9" class="s">
            <template #default="{ expanded }">
              <b-icon
                v-if="expanded"
                icon="chevron-bar-up"
                font-scale="1.5"
              ></b-icon>
              <b-icon v-else icon="chevron-bar-down" font-scale="1"></b-icon>
            </template>
          </b-navbar-toggle>
          <b-collapse id="navbar-toggle-collapse9" is-nav>
            <b-navbar-nav class="u">
              <b-nav-item>
                <p class="t" style="text-indent: 70px; margin-top: 10px">
                  โรคติดเชื้อบริเวณหัวใจทั้ง 3 ชนิด ได้แก่ เยื่อหุ้มหัวใจอักเสบ
                  กล้ามเนื้อหัวใจอักเสบ และลิ้นหัวใจอักเสบ
                  มีสาเหตุมาจากสิ่งก่อความระคายเคืองอย่างเชื้อไวรัส แบคทีเรีย
                  ปรสิต หรือสารเคมีที่แพร่เข้าไปยังหัวใจ
                  และเป็นสาเหตุของการติดเชื้อในที่สุด
                </p>
              </b-nav-item>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>

        <p class="p">ปัจจัยเสี่ยงโรคหัวใจ</p>
        <ul class="w">
          <li class="q">อายุมากขึ้น</li>
          <li class="q">บุคคลในครอบครัวเป็นโรคหัวใจ</li>
          <li class="q">โรคเบาหวาน</li>
          <li class="q">โรคอ้วน</li>
          <li class="q">ความดันโลหิตสูง</li>
          <li class="q">ระดับคอเลสเตอรอลในเลือดสูง</li>
          <li class="q">การสูบบุหรี่</li>
          <li class="q">ไม่ออกกำลังกาย</li>
          <li class="q">ความเครียด</li>
        </ul>

        <p class="p">วิธีการรักษา</p>
        <p class="q">
          โรคหัวใจที่มีหลากหลายชนิดก็มีวิธีรักษาแตกต่างกัน
          แต่โดยทั่วไปแล้วมีวิธีรักษา ดังนี้
        </p>
        <ul class="w">
          <li class="q">
            ปรับพฤติกรรมการใช้ชีวิตเช่น รับประทานอาหารไขมันต่ำและอาหารโซเดียมต่ำ
            ออกกำลังกายแบบพอประมาณอย่างน้อย 30 นาที สัปดาห์ละ 5 วัน
            รวมทั้งเลิกสูบบุหรี่และลดปริมาณการดื่มแอลกอฮอล์
          </li>
          <li class="q">ใช้ยารักษา</li>
          <li class="q">ใช้กระบวนการทางแพทย์หรือการผ่าตัดรักษา</li>
        </ul>

        <b-card-group deck style="margin-top: 50px">
          <b-card
            img-src="~assets/33.jpg"
            img-alt="Image"
            img-top
            img-height="400px"
            style="max-width: 50rem"
          >
            <b-card-text
              style="font-family: 'K2D', sans-serif; font-size: 25px"
            >
              ควรงดการสูบุหรี่เพื่อสุขภาพหัวใจที่ดีขึ้นของท่าน
            </b-card-text>
          </b-card>

          <b-card
            img-src="~assets/22.jpg"
            img-alt="Image"
            img-top
            img-height="400px"
            style="max-width: 50rem"
          >
            <b-card-text
              style="font-family: 'K2D', sans-serif; font-size: 25px"
            >
              ควรดื่มสุราให้น้อยลงหรือเลิกดื่มสุราเพื่อสุขภาพหัวใจที่ดีขึ้นของท่าน
            </b-card-text>
          </b-card>
        </b-card-group>

        <p class="q" style="padding-top: 30px">
          ที่มา：
          <b-link
            href="https://www.paolohospital.com//th-TH/chokchai4/Article/Details/โรคหัวใจ/เรื่อง--โรคหัวใจ--ทำไมต้องรู้"
            >โรงพยาบาลเปาโล</b-link
          >
        </p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  layout: 'headerguest',
  middlewares: 'notAdmin',
}
</script>

<style>
/* import font Kanit */
@import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
/* import font K2D */
@import url('https://fonts.googleapis.com/css2?family=K2D:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800&display=swap');

.b {
  color: darkslategray;
  font-family: 'K2D', sans-serif;
  font-size: 45px;
  text-align: center;
}

.p {
  color: black;
  font-family: 'K2D', sans-serif;
  font-size: 30px;
  font-weight: bold;
  margin-top: 50px;
}

.q {
  color: darkslategray;
  font-family: 'K2D', sans-serif;
  font-size: 25px;
}

.r {
  color: black;
  font-family: 'K2D', sans-serif;
  font-size: 25px;
  font-weight: bold;
  margin-left: 20px;
}

.s {
  margin-right: auto;
  margin-bottom: 15px;
  border-width: 3px;
  border-color: black;
}

.t {
  color: darkslategray;
  font-family: 'K2D', sans-serif;
  font-size: 25px;
  margin-left: 20px;
  margin-right: 20px;
}

.u {
  background-color: rgb(243, 243, 243);
  border-style: ridge;
  border-width: 3px;
}

ul.w {
  list-style-position: outside;
}

.v {
  color: darkslategray;
  font-family: 'K2D', sans-serif;
  font-size: 25px;
  margin-left: 40px;
  margin-right: 20px;
}

.x {
  padding-right: 20px;
}
</style>
