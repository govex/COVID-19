import pandas
import plotly.express as express_plot

data_frame = pandas.read_csv('data_tables/vaccine_data/us_data/time_series/vaccine_data_us_timeline.csv')

graph = express_plot.line(
    data_frame, 
    x = 'Date', 
    y = 'Doses_admin', 
    title='COVID vaccination rate over time',
    color="Province_State")
graph.show()