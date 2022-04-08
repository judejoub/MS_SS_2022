from pm4py.objects.conversion.log import converter as log_converter
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
import graphviz

from Beginning import load_data, new_features

data = load_data()
datalog = new_features(data)
datalog.rename(columns={'exe_soi_dtd': 'time:timestamp','patient_id': 'case:concept:name', 'code': 'concept:name'}, inplace=True)
datalog = datalog[datalog["case:concept:name"]=='496']
## Convert to log format
log = log_converter.apply(datalog)

# Alpha_miner algorithm
net, initial_marking, final_marking = alpha_miner.apply(log)

# Visualise this model as a petri net
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)

#

