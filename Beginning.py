import random as random
import pandas as pd
import datetime
from datetime import timedelta
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as seaborn
import numpy as np
import re

def load_data():
    _input_path = Path("/Users/eloijoubert/Desktop/CREST/data_mort_subite.csv")
    input_data = pd.read_csv(filepath_or_buffer= _input_path, sep=';', )
    return input_data

def reduce_string(string):
    return string[:-1]

def category_cmi(x):
    if x == "" :
        return 0
    elif x[0] in ['A','B']:
        return 1
    elif x[0] == 'C':
        return 2
    elif x[0] == 'D':
        if float(x[1])<5:
            return 2
        else :
            return 3
    elif x[0] == 'E':
        return 4
    elif x[0] == 'F' :
        return 5
    elif x[0] == 'G' :
        return 6
    elif x[0] == 'H' :
        if float(x[1])<6:
            return 7
        else :
            return 8
    elif x[0] == 'I' :
        return 9
    elif x[0] == 'J':
        return 10
    elif x[0] == 'K':
        return 11
    elif x[0] == 'L':
        return 12
    elif x[0] == 'M':
        return 13
    elif x[0] == 'N':
        return 14
    elif x[0] == 'O':
        return 15
    elif x[0] == 'P':
        return 16
    elif x[0] == 'Q':
        return 17
    elif x[0] == 'R':
        return 18
    elif x[0] in ['S', 'T']:
        return 19
    elif x[0] in ['V', 'Y']:
        return 20
    elif x[0] == 'Z':
        return 21
    elif x[0] == 'U':
        return 22

def new_features(data):

    data = data[["num_enq", "exe_soi_dtd", "code"]].copy()

    # Date in datetime format , Creation day, month, year, weekday

    data["exe_soi_dtd"] = pd.to_datetime(data["exe_soi_dtd"], format= "%Y-%m-%d")
    #data["jour"] = data["exe_soi_dtd"].dt.day
    #data["mois"] = data["exe_soi_dtd"].dt.month
    #data["année"] = data["exe_soi_dtd"].dt.year
    #data["jour_semaine"] = data["exe_soi_dtd"].dt.weekday

    # Creation patient_il column

    data["patient_id"]=[str(i.replace('NUM-PATIENT-CEMS-',"")) for i in data["num_enq"]]

    # Creation new_code

    data['new_code_PHA']= [str(i.replace('PHA_',"")) for i in data["code"]]
    data['new_code_PHA'] = [re.sub('PMSI_.*','',i) for i in data["new_code_PHA"]]
    data["new_code_PHA"] = data["new_code_PHA"].astype(str)


    data['new_code_PMSI']=[str(i.replace('PMSI_',"")) for i in data["code"]]
    data['new_code_PMSI'] = [re.sub('PHA_.*','',i) for i in data["new_code_PMSI"]]
    data["new_code_PMSI"] = data["new_code_PMSI"].astype(str)

    # Creation des groupes

    data['new_code_cmi'] = data['new_code_PHA'].apply(reduce_string)
    data["category_cmi"] = data["new_code_cmi"] + data["new_code_PMSI"]
    data['category_cmi'] = data['category_cmi'].apply(category_cmi)
    data["category_cmi"] = data["category_cmi"].astype(str)

    return data


data = pd.DataFrame(load_data())
data = new_features(data).sort_values(by = 'exe_soi_dtd', ascending= True)
print(data.category_cmi.dtypes)
print(f'Nombre de ref PMSI dans dataframe : {data[data["new_code_PMSI"] !=""].shape[0]}')


#x = random.choices(data["patient_id"].unique(), k = 10)
#print(x)
#print(data["code"].unique())

