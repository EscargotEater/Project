<template>
  <div>
    <b-container class="my-5">
      <b-row style="font-family: 'K2D', sans-serif">
        <b-col cols="12">
          <h1 style="color: darkslategray">อัพเดตโมเดล</h1>
          <hr class="mt-3 mb-5" />
        </b-col>
        <b-col cols="12">
          <b-overlay :show="show" rounded="sm" variant="light">
            <b-card>
              <b-alert v-if="message" show variant="success">
                {{ message }}
              </b-alert>
              <b-alert v-if="alert" show variant="danger">{{ alert }}</b-alert>
              <b-form-group
                style="font-size: 20px"
                label="โมเดลตรวจโรคเบาหวานและโรคหัวใจ"
                label-cols-sm="4"
              >
                <b-form-file
                  v-model="file"
                  accept=".csv"
                  placeholder="กดที่ปุ่ม 'ค้นหา' เพื่อเลือกไฟล์"
                  browse-text="ค้นหา"
                  class="mb-4"
                ></b-form-file>
              </b-form-group>
              <b-button variant="warning" @click="file = null">รีเซ็ต</b-button>
              <b-button variant="primary" class="ml-2" @click="submit"
                >อัพเดต</b-button
              >
            </b-card>
          </b-overlay>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  layout: 'headerguest',
  middleware: ['admin'],
  data() {
    return {
      file: null,
      alert: null,
      message: null,
      show: false,
    }
  },
  methods: {
    async submit() {
      this.alert = null
      this.message = null
      try {
        this.show = true
        const formData = new FormData()
        formData.append('file', this.file)
        const response = await axios.post(
          'http://localhost:5000/update/',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          }
        )
        this.show = false
        this.message = response.data.message
      } catch (e) {
        this.show = false
        this.alert = 'มีข้อผิดพลาดในการอัพเดทโมเดล'
      }
    },
  },
}
</script>
