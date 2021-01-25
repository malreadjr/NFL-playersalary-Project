function buildPlot() {
  /* data route */
  const url = "/api/salaries";
  d3.json(url).then(function(data) {

    console.log(data);

function calcAvg(year_no) {
  let results = data.filter((item) => {
    return item.year === year_no;
  })

  let salary = results.map((item) => {
    return item.salary;
  })
  
  var total = 0;
  for(var i = 0; i < salary.length; i++) {
      total += salary[i];
  }
  var avg = total / salary.length;

  return avg;

}

console.log(calcAvg(2015))

var trace = {
  type: "scatter",
  mode: "lines",
  // name: name,
  x: [2015, 2016, 2017, 2018, 2019, 2020],
  y: [calcAvg(2015), calcAvg(2016), calcAvg(2017), calcAvg(2018), calcAvg(2019), calcAvg(2020)],
  line: {
    color: "#17BECF"
  }
};



var data = [trace];

var layout = {
  title: `Salary Data`,
  // xaxis: {
  //   range: [startDate, endDate],
  //   type: "date"
  // },
  // yaxis: {
  //   autorange: true,
  //   type: "linear"
  // },
  showlegend: false
};

Plotly.newPlot("plot", data, layout);


  })

//   .catch(function(error){
//     // handle error   
//  })
}

buildPlot();