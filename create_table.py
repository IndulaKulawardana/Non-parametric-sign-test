import plotly
import plotly.graph_objs as go


def create_table(results, file_path):

    trace = go.Table(
        header=dict(values=list(results.keys()),
                    fill=dict(color='#c2f0f0'),
                    align=['left'] * 5),
        cells=dict(values=list(results.values()),
                   fill=dict(color='#c2f0f0'),
                   align=['left'] * 5))

    table_data = [trace]
    plotly.offline.plot({'data': table_data}, filename=file_path)
