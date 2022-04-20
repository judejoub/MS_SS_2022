from pm4py.objects.conversion.log import converter as log_converter
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.visualization.process_tree import visualizer as pt_visualizer

from Beginning import load_data, new_features

data = load_data()
datalog = new_features(data)
datalog.rename(columns={'date': 'time:timestamp','patient_id': 'case:concept:name', 'code': 'concept:name'}, inplace=True)

## Convert to log format
log = log_converter.apply(datalog)

#Alpha_miner algorithm
net, initial_marking, final_marking = alpha_miner.apply(log)
gviz1 = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz1)

#Heuristic miner
heu_net = heuristics_miner.apply_heu(log)
gviz3 = hn_visualizer.apply(heu_net)
hn_visualizer.view(gviz3)

#Inductive miner
tree = inductive_miner.apply_tree(log)
gviz4 = pt_visualizer.apply(tree)
pt_visualizer.view(gviz4)
