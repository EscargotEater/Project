<template>
  <div class="box">
    <p class="bigmsg">ระบบลงทะเบียน</p>
    <hr class="solid" />

    <p class="desc">กรุณากรอกข้อมูลเพื่อทำการลงทะเบียน</p>

    <b-alert v-if="error" show variant="danger">{{ error }}</b-alert>
    <p class="fieldname">อีเมล</p>
    <b-input-group class="mb-2" size="lg">
      <b-input-group-prepend is-text>
        <b-icon icon="envelope-fill"></b-icon>
      </b-input-group-prepend>
      <b-form-input
        v-model="$v.form.email.$model"
        :class="{ hasError: $v.form.email.$error }"
        class="msg"
        type="text"
        placeholder="โปรดกรอกอีเมลของท่านลงในช่องนี้"
        @input="$v.form.email.$touch()"
      ></b-form-input>
    </b-input-group>
    <div v-if="!$v.form.email.required && $v.form.email.$dirty" class="error">
      กรุณากรอกอีเมล์
    </div>
    <div v-if="!$v.form.email.email" class="error">อีเมล์ไม่ถูกต้อง</div>

    <p class="fieldname">รหัสผ่าน</p>
    <b-input-group class="mb-2" size="lg">
      <b-input-group-prepend is-text>
        <b-icon icon="person-fill"></b-icon>
      </b-input-group-prepend>
      <b-form-input
        v-model="$v.form.password.$model"
        :class="{ hasError: $v.form.password.$error }"
        class="msg"
        type="password"
        placeholder="โปรดกรอกรหัสผ่านของท่านลงในช่องนี้"
        @input="$v.form.password.$touch()"
      ></b-form-input>
    </b-input-group>
    <div
      v-if="!$v.form.password.required && $v.form.password.$dirty"
      class="error"
    >
      กรุณากรอกรหัสผ่าน
    </div>
    <div v-if="!$v.form.password.minLength" class="error">
      กรุณากรอกรหัสผ่านอย่างน้อย
      {{ $v.form.password.$params.minLength.min }} ตัวอักษร
    </div>

    <p class="fieldname">ยืนยันรหัสผ่าน</p>
    <b-input-group class="mb-2" size="lg">
      <b-input-group-prepend is-text>
        <b-icon icon="person-fill"></b-icon>
      </b-input-group-prepend>
      <b-form-input
        v-model="$v.form.repassword.$model"
        :class="{ hasError: $v.form.repassword.$error }"
        class="msg"
        type="password"
        placeholder="โปรดยืนยันรหัสผ่านของท่านลงในช่องนี้"
        @input="$v.form.repassword.$touch()"
      ></b-form-input>
    </b-input-group>
    <div
      v-if="!$v.form.repassword.required && $v.form.repassword.$dirty"
      class="error"
    >
      กรุณายืนยันรหัสผ่าน
    </div>
    <div
      v-if="!$v.form.repassword.sameAsPassword && $v.form.repassword.required"
      class="error"
    >
      รหัสผ่านไม่ตรงกัน
    </div>

    <p class="fieldname">ชื่อ</p>
    <b-input-group class="mb-2" size="lg">
      <b-input-group-prepend is-text>
        <b-icon icon="person-circle"></b-icon>
      </b-input-group-prepend>
      <b-form-input
        v-model="$v.form.firstName.$model"
        :class="{ hasError: $v.form.firstName.$error }"
        class="msg"
        type="text"
        placeholder="โปรดกรอกชื่อของท่านลงในช่องนี้"
        @input="$v.form.firstName.$touch()"
      ></b-form-input>
    </b-input-group>
    <div
      v-if="!$v.form.firstName.required && $v.form.firstName.$dirty"
      class="error"
    >
      กรุณากรอกชื่อ
    </div>

    <p class="fieldname">นามสกุล</p>
    <b-input-group class="mb-2" size="lg">
      <b-input-group-prepend is-text>
        <b-icon icon="person-circle"></b-icon>
      </b-input-group-prepend>
      <b-form-input
        v-model="$v.form.lastName.$model"
        :class="{ hasError: $v.form.lastName.$error }"
        class="msg"
        type="text"
        placeholder="โปรดกรอกนามสกุลของท่านลงในช่องนี้"
        @input="$v.form.lastName.$touch()"
      ></b-form-input>
    </b-input-group>
    <div
      v-if="!$v.form.lastName.required && $v.form.lastName.$dirty"
      class="error"
    >
      กรุณากรอกนามสกุล
    </div>

    <b-button
      type="submit"
      value="submit"
      variant="outline-warning"
      style="
        display: block;
        font-family: 'K2D', sans-serif;
        font-size: 20px;
        font-weight: bold;
        letter-spacing: 0.5px;
        border-width: 3px;
        border-radius: 5px;
        transition-duration: 0.4s;
        padding: 10px 15px;
        margin-left: auto;
        margin-right: auto;
        margin-top: 20px;
        text-align: center;
      "
      @click="regis"
    >
      ลงทะเบียน
    </b-button>
    <div class="login mb-5">
      มีบัญชีอยู่แล้ว? <b-link to="/login">เข้าสู่ระบบ</b-link>
    </div>
  </div>
</template>

<script>
import { required, minLength, email, sameAs } from 'vuelidate/lib/validators'

export default {
  layout: 'headerguest',
  data() {
    return {
      form: {
        email: '',
        password: '',
        repassword: '',
        firstName: '',
        lastName: '',
      },
      error: '',
    }
  },
  validations: {
    form: {
      email: {
        email,
        required,
      },
      password: {
        minLength: minLength(6),
        required,
      },
      repassword: {
        required,
        sameAsPassword: sameAs('password'),
      },
      firstName: {
        required,
      },
      lastName: {
        required,
      },
    },
  },
  methods: {
    async regis() {
      if (!this.$v.form.$anyError) {
        try {
          await this.$axios.post('auth/local/register', {
            username: this.form.email,
            email: this.form.email,
            password: this.form.password,
            FirstName: this.form.firstName,
            LastName: this.form.lastName,
          })
          await this.$axios.post('activities', {
            activity: 'register',
          })
          await this.$auth.loginWith('local', {
            data: {
              identifier: this.form.email,
              password: this.form.password,
            },
          })
          this.$toast.success('ลงทะเบียนสำเร็จ')
        } catch (e) {
          if (e.response?.data?.message[0]?.messages[0]?.message) {
            const errorMessage =
              'ลงทะเบียนไม่สำเร็จ : ' +
              e.response?.data?.message[0]?.messages[0]?.message
            console.error(errorMessage)
            this.error = errorMessage
          } else {
            const errorMessage = 'เข้าสู่ระบบไม่สำเร็จ : ' + e
            console.error(errorMessage)
            this.error = errorMessage
          }
        }
      }
    },
  },
}
</script>

<style>
/* import font Kanit */
@import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
/* import font K2D */
@import url('https://fonts.googleapis.com/css2?family=K2D:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800&display=swap');
.bigmsg {
  color: darkslategray;
  font-family: 'K2D', sans-serif;
  font-size: 40px;
  text-align: center;
  padding-top: 120px;
  font-weight: bold;
}
.box {
  margin: auto;
  width: 60%;
  padding: 10px;
}
.desc {
  color: black;
  font-family: 'K2D', sans-serif;
  font-size: 25px;
  font-weight: bold;
  margin-top: 30px;
  text-align: center;
}
.fieldname {
  margin-top: 20px;
  color: darkslategray;
  font-family: 'K2D', sans-serif;
  font-size: 20px;
}
.login {
  font-family: 'K2D', sans-serif;
  font-size: 20px;
  font-weight: bold;
  margin-top: 20px;
  text-align: center;
}
.msg {
  font-family: 'K2D', sans-serif;
  font-size: 20px;
}
.error {
  color: red;
}
</style>
