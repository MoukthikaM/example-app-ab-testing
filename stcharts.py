from streamlit_echarts import st_echarts

options = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}
    ],
}
st_echarts(options=options)


from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

b = (
    Bar()
    .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
    .add_yaxis(
        "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)


options = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": [
                120,
                {"value": 200, "itemStyle": {"color": "#a90000"}},
                150,
                80,
                70,
                110,
                130,
            ],
            "type": "bar",
        }
    ],
}
st_echarts(
    options=options,
    height="400px",
)
