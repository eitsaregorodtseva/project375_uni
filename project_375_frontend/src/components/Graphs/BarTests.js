import { Bar } from 'vue-chartjs'
export default {
  extends: Bar,
  mounted () {
    this.renderChart({
      labels: ['Верно', 'Неверно'],
      datasets: [
        {
          label: 'Количество ответов',
          backgroundColor: ['#2ea44f', '#dd4b39'],
          barPercentage: 0.4,
          data: [5, 8, 0, 15]
        }
      ]
    }, {responsive: true, maintainAspectRatio: false})
  }
}
