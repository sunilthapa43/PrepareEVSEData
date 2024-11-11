import os
from manager.config import EVSE_ROOT
import pandas as pd

file_path = EVSE_ROOT + "network_data_combined.csv"

df = pd.read_csv(file_path)
#  checking if all data is present
print(df[df["State"]== "Idle"])