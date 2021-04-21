import { Line } from 'vue-chartjs'
export default {
  extends: Line,
  mounted () {
    this.renderChart({
      labels: ['Январь', 'Февраль', 'Март', 'Апрель'],
      datasets: [
        {
          label: 'Количество пройденных тестов',
          backgroundColor: '#9acd32',
          barPercentage: 0.2,
          data: [10, 3, 5, 4, 0, 15]
        }
      ]
    }, {responsive: true, maintainAspectRatio: false})
  }
}
