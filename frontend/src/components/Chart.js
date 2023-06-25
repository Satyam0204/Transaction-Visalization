"use client";
import React,{useState,useEffect} from 'react'
import ReactEcharts from "echarts-for-react"; 

const Chart = () => {
    const [Xdata, setXdata] = useState();
    const [Ydata, setYdata] = useState();

    useEffect(() => {
      gettransactions()
  }, []);

    const gettransactions=async()=>{
        let response = await fetch('http://localhost:5000/',{
            method:'GET',
            headers:{
                'Content-Type':'application/json'
            }
        })
        let data= await response.json()
        setXdata(Object.keys(data))
        setYdata(Object.values(data))
        console.log(data)
    }

    var options = {
      title: {
        text: 'Average Transaction per Block',
      },
      legend: {},
      tooltip: {},
      xAxis: {
        type: 'category',

        data: Xdata,
      },
      yAxis: {
        type: 'value',
      },
      series: [
        {
          name: 'Average Transaction per Block',
          type: 'line',
          data: Ydata,
          areaStyle: {}
        },
      ],
    };
    
    
  return (
    <div>
      this is chart component

      <ReactEcharts option={options} />
    </div>
  )
}

export default Chart
