
from fmpy.util import plot_result  # import the plot function
from fmpy import *
import numpy as np
#import matplotlib
import plotly.graph_objects as go

fmu = 'PumpingSystemFMU'
fmu = 'valve.fmu'
dump(fmu)  # get information
#input_values = {'ATE': 1}

result = simulate_fmu(fmu)         # simulate the FMU
plot_result(result)
