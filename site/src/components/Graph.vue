<template>
    <Highcharts :options="chartOptions"></Highcharts>
</template>

<script>
    import {Chart} from 'highcharts-vue'

    export default {
        name: "Graph.vue",
        components: {
            Highcharts: Chart
        },
        data() {
            return {
                chartOptions: {
                    chart: {
                        type: 'column',
                        pointWidth: 20
                    },
                    title: {
                        text: 'Most Frequent K Algorithm'
                    },
                    series: [{
                        data: [{
                            x: 1,
                            y: 1,
                            name: "A",
                            color: "#7CDEDC"
                        }, {
                            x: 2,
                            y: 2,
                            name: "B",
                            color: "#7284A8"
                        }]
                    }],
                    xAxis: {
                        visible: false
                    },
                    yAxis: {
                        title: {
                            text: 'Count'
                        },
                        tickInterval: 1
                    },
                    plotOptions: {
                        column: {
                            dataSorting: {
                                enabled: true
                            },
                            pointPadding: 0.1,
                            pointWidth: 20,
                        }
                    }
                }
            }
        },
        computed : {
            graphData() {
                let data = [];
                const alpha = "ABCDEFGHIJKLMNOPQRST";
                for (let i=0; i<10; i++) {
                    data.push({
                        x: i+1,
                        y: i+1,
                        name: alpha[i],
                        color: i%2 === 0 ? "#7CDEDC" : "#7284A8"
                    })
                }
                return data
            }
        }
    }


</script>

<style scoped>
    input[type="color"]::-webkit-color-swatch-wrapper {
        padding: 0;
    }

    #colorPicker {
        border: 0;
        padding: 0;
        margin: 0;
        width: 30px;
        height: 30px;
    }

    .numberInput {
        width: 30px;
    }
</style>