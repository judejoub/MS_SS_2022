import pandas as pd
import datetime
from datetime import timedelta
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as seaborn
import numpy as np

def load_data():
    _input_path = Path("/Users/eloijoubert/Desktop/CREST/mort_subite/data_mort_subite.csv")
    input_data = pd.read_csv(filepath_or_buffer= _input_path, sep=';', )
    return input_data

def new_features(data):

    data = data[["num_enq", "exe_soi_dtd", "code"]].copy()

    # Date in datetime format , Creation day, month, year, weekday

    data["exe_soi_dtd"] = pd.to_datetime(data["exe_soi_dtd"], format= "%Y-%m-%d")
    data["jour"] = data["exe_soi_dtd"].dt.day
    data["mois"] = data["exe_soi_dtd"].dt.month
    data["année"] = data["exe_soi_dtd"].dt.year
    data["jour_semaine"] = data["exe_soi_dtd"].dt.weekday

    # Creation patient_il column

    data["patient_id"]=[str(i.replace('NUM-PATIENT-CEMS-',"")) for i in data["num_enq"]]

    # Creation new_code

    data['new_code']=[str(i.replace('PHA_',"")) for i in data["code"]]

    return data

data = pd.DataFrame(load_data())
data = new_features(data).sort_values(by = 'exe_soi_dtd', ascending= True)

print(data)
