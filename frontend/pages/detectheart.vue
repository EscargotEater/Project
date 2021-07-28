<template>
  <b-container class="my-5">
    <p class="b">ตรวจโรคหัวใจ</p>
    <hr class="mt-3 mb-5" />
    <b-alert
      show
      dismissible
      variant="danger"
      style="
          font-family: 'K2D', sans-serif;
          font-size: 22px;
          padding-top: 20px;
          mx-auto;
        "
      ><h4 class="alert-heading">คุณมีค่า"คอเลสเตอรอล"สูงกว่าเกณฑ์!</h4>

      <p>
        คำแนะนำ: ลดอาหารที่มีไขมันนอิ่มตัว เช่น เนื้อสัตว์ติดมัน งดแอลกอฮอล์
        ออกกำลังกายเป็นประจำ
      </p>
    </b-alert>
    <b-card
      border-variant="primary"
      header="โปรดกรอกข้อมูลผลตรวจสุขภาพประจำปี"
      header-bg-variant="primary"
      header-text-variant="white"
      bg-variant="light"
      body-class="text-center"
      align="center"
      style="
          color: darkslategray;
          font-family: 'K2D', sans-serif;
          font-size: 22px;
          margin-top: 50px;
          mx-auto;
        "
    >
      <b-alert v-if="message" show variant="success">{{ message }}</b-alert>
      <b-alert v-if="alert" show variant="danger">{{ alert }}</b-alert>
      <b-row class="mb-3" align-v="center" align-h="end">
        <b-col sm="5">อายุ</b-col>
        <b-col sm="2">
          <b-form-input v-model="value.age" type="number" inline></b-form-input>
        </b-col>
        <b-col sm="5">ปี</b-col>

        <b-col cols="12"><hr class="my-2" /></b-col>

        <b-col sm="5">
          <b-card-text> ระดับน้ำตาลในเลือด </b-card-text>
        </b-col>
        <b-col sm="2">
          <b-form-input
            id="glucose"
            v-model="value.fbs"
            type="number"
            inline
          ></b-form-input>
        </b-col>
        <b-col sm="5"> มิลลิลิตร/เดซิลิตร </b-col>

        <b-col cols="12"><hr class="my-2" /></b-col>

        <b-col sm="5">
          <b-card-text> ความยาวรอบเอว </b-card-text>
        </b-col>
        <b-col sm="2">
          <b-form-input
            id="waist"
            v-model="value.waist"
            type="number"
            inline
          ></b-form-input>
        </b-col>
        <b-col sm="5"> เซนติเมตร </b-col>

        <b-col cols="12"><hr class="my-2" /></b-col>

        <b-col sm="5"> ความดันสูงสุดขณะหัวใจบีบตัว </b-col>
        <b-col sm="2">
          <b-form-input
            id="pressurehigh"
            v-model="value.bpsy"
            type="number"
            inline
          ></b-form-input>
        </b-col>
        <b-col sm="5"> มิลลิเมตร.ปรอท </b-col>

        <b-col cols="12"><hr class="my-2" /></b-col>

        <b-col sm="5"> ความดันต่ำสุดขณะหัวใจคลายตัว </b-col>
        <b-col sm="2">
          <b-form-input
            id="pressureสนไ"
            v-model="value.bpdi"
            type="number"
            inline
          ></b-form-input>
        </b-col>
        <b-col sm="5"> มิลลิเมตร.ปรอท </b-col>

        <b-col cols="12"><hr class="my-2" /></b-col>

        <b-col sm="5">
          <b-card-text> คอเรสเตอรอลทั้งหมด </b-card-text>
        </b-col>
        <b-col sm="2">
          <b-form-input
            id="chloresterolall"
            v-model="value.tchol"
            type="number"
            inline
          ></b-form-input>
        </b-col>
        <b-col sm="5"> มิลลิกรัม.เดซิลิตร </b-col>

        <b-col cols="12"><hr class="my-2" /></b-col>

        <b-col sm="5"> คอเรสเตอรอลHDL </b-col>
        <b-col sm="2">
          <b-form-input
            id="hdl"
            v-model="value.hdl"
            type="number"
            inline
          ></b-form-input>
        </b-col>
        <b-col sm="5"> มิลลิกรัม.เดซิลิตร </b-col>

        <b-col cols="12"><hr class="my-2" /></b-col>

        <b-col cols="5">มีญาติเป็นโรคเบาหวาน</b-col>
        <b-col cols="2" class="m-0 mt-3">
          <b-form-group v-slot="{ ariaDescribedby }">
            <b-form-radio-group
              id="radio-group-2"
              v-model="value.dbfam"
              :aria-describedby="ariaDescribedby"
              name="radio-sub-component"
            >
              <b-form-radio value="1"> มี </b-form-radio>
              <b-form-radio value="0"> ไม่มี </b-form-radio>
            </b-form-radio-group>
          </b-form-group>
        </b-col>
        <b-col cols="5">-</b-col>
      </b-row>
    </b-card>

    <b-button
      sm="5"
      type="submit"
      size="lg"
      variant="primary"
      align="center"
      style="
        margin-left: 40%;
        margin-top: 30px;
        font-family: 'K2D', sans-serif;
        font-size: 25px;
      "
      @click="submit"
      >ประเมินความเสี่ยง
    </b-button>
  </b-container>
</template>

<script>
export default {
  layout: 'headerguest',
  middlewares: 'notAdmin',
  data() {
    return {
      value: {
        age: 50,
        fbs: 100,
        waist: 70,
        bpsy: 120,
        bpdi: 80,
        tchol: 175,
        hdl: 50,
        dbfam: 0,
      },
      message: '',
      alert: '',
    }
  },
  methods: {
    async submit() {
      this.message = null
      this.alert = null
      const res = await this.$axios.post('predict/cad', {
        fbs: this.value.fbs,
        waist: this.value.waist,
        age: this.value.age,
        bpsy: this.value.bpsy,
        bpdi: this.value.bpdi,
        tchol: this.value.tchol,
        hdl: this.value.hdl,
        dbfam: this.value.dbfam,
      })
      res.data === 0
        ? (this.message = 'ยินดีด้วย ตรวจไม่พบโรคหัวใจ')
        : (this.alert =
            'ตรวจพบโรคเบาหวาน ควรไปพบแพทย์เพื่อทำการตรวจโดยละเอียดอีกครั้ง')
      await this.$axios.post('activities', {
        activity: 'predictcad',
      })
    },
  },
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
  font-size: 40px;
  text-align: center;
}
</style>
