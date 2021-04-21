import { Pie } from 'vue-chartjs'
export default {
  extends: Pie,
  mounted () {
    this.renderChart({
      labels: ['Тест на оперативную память 1', 'Тест на оперативную память 2'],
      datasets: [
        {
          label: 'Количество прохождений',
          backgroundColor: ['#ff6d29', '#ff74ca'],
          barPercentage: 0.4,
          data: [1, 8]
        }
      ]
    }, {responsive: true, maintainAspectRatio: false})
  }
}
