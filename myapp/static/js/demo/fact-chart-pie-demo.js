// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Pagadas", "No pagadas", "Anuladas"],
    datasets: [{
      data: [95, 3, 2],
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {
        label: function (tooltipItem, data) {
          var dataset = data.datasets[tooltipItem.datasetIndex];
          var total = dataset.data.reduce(function (previousValue, currentValue) {
            return previousValue + currentValue;
          });
          var currentValue = dataset.data[tooltipItem.index];
          var percentage = ((currentValue / total) * 100).toFixed(0);
          return percentage + '%';
        }
      }
    },
    legend: {
      display: true,
      position: 'bottom',
      labels: {
        usePointStyle: true,
        fontColor: '#858796',
      },
    },
    cutoutPercentage: 80,
  },
});