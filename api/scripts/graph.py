import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from api.models import Times
import io
import base64

def getting_graph():
    time_id = list(Times.objects.values_list('id', flat=True))
    if time_id == None:
        return None
    else:
        time_measured = list(Times.objects.values_list('time', flat=True))
        time_floats = [float(t) for t in time_measured]

        fig, ax = plt.subplots()
        ax.plot(time_id, time_floats)

        ax.set(xlabel='id(s)', ylabel='time(s)',
            title='Measured time of requests')
        ax.grid()

        buffer = io.BytesIO() 
        fig.savefig(buffer, format='png') 
        buffer.seek(0)
        graph_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        return graph_base64

