<script>
import { Line } from 'vue-chartjs'
export default {
  extends: Line,
  props: {
    data: { type: Array, default: null },
  },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [
          {
            label: 'อายุ (ปี)',
            borderColor: '#EC4899',
            backgroundColor: '#EC489900',
            data: [],
          },
          {
            label: 'ระดับน้ำตาลในเลือด (มล./ดล.)',
            borderColor: '#EF4444',
            backgroundColor: '#EC489900',
            data: [],
          },
          {
            label: 'ความยาวรอบเอว (ซม.)',
            borderColor: '#F59E0B',
            backgroundColor: '#EC489900',
            data: [],
          },
          {
            label: 'ความดันสูงสุดขณะหัวใจบีบตัว (มม.ปรอท)',
            borderColor: '#10B981',
            backgroundColor: '#EC489900',
            data: [],
          },
          {
            label: 'ความดันต่ำสุดขณะหัวใจคลายตัว (มม.ปรอท)',
            borderColor: '#3B82F6',
            backgroundColor: '#EC489900',
            data: [],
          },
          {
            label: 'คลอเรสเตอรอลทั้งหมด (มก./ดล.)',
            borderColor: '#6366F1',
            backgroundColor: '#EC489900',
            data: [],
          },
          {
            label: 'คลอเรสเตอรอล HDL (มก./ดล.)',
            borderColor: '#8B5CF6',
            backgroundColor: '#EC489900',
            data: [],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        elements: {
          line: {
            tension: 0,
          },
        },
        legend: {
          position: 'top',
          labels: {
            fontSize: 15,
            fontFamily: 'K2D',
          },
        },
        title: {
          display: false,
          text: 'ประวัติการตรวจโรคหัวใจ',
          fontSize: 15,
          fontFamily: 'K2D',
        },
      },
    }
  },
  watch: {
    data(val) {
      this.chartData.labels = []
      this.chartData.datasets[0].data = []
      this.chartData.datasets[1].data = []
      this.chartData.datasets[2].data = []
      this.chartData.datasets[3].data = []
      this.chartData.datasets[4].data = []
      this.chartData.datasets[5].data = []
      this.chartData.datasets[6].data = []
      this.init(val)
      this.renderChart(this.chartData, this.options)
    },
  },
  mounted() {
    this.init(this.data)
    this.renderChart(this.chartData, this.options)
  },
  methods: {
    init(data) {
      for (let i = 0; i < data.length; i++) {
        this.chartData.datasets[0].data.push(data[i].age)
        this.chartData.datasets[1].data.push(data[i].fbs)
        this.chartData.datasets[2].data.push(data[i].waist)
        this.chartData.datasets[3].data.push(data[i].bpsy)
        this.chartData.datasets[4].data.push(data[i].bpdi)
        this.chartData.datasets[5].data.push(data[i].tchol)
        this.chartData.datasets[6].data.push(data[i].hdl)
        this.chartData.labels.push(
          new Date(data[i].created_at).toLocaleString()
        )
      }
    },
  },
}
</script>
