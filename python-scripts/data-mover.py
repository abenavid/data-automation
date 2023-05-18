import datetime
import shutil
import os
import pandas as pd

# Note - use '/' instead of '\' on paths
tmp_dir_path = ""  # TODO update tmp dir path to your folder which will feed data to SSIS project
data_dir_path = ""  # TODO update data dir path to the folder where your .csv files exist

old_file = os.listdir(tmp_dir_path)

data_files = [f for f in os.listdir(data_dir_path) if '.csv' in f.lower()]
new_file = data_files[-1] # use 0 for first, use -1 for last (the purpose of this is to grab the .csv files in order)

if old_file[0] != new_file:
  shutil.rmtree(tmp_dir_path)
  os.mkdir(tmp_dir_path)
  df = pd.read_csv(data_dir_path + '/' + new_file)
  df['Time']=pd.to_datetime(df['Time']).apply(lambda s:s.isoformat())
  df.to_csv(data_dir_path + '/' + new_file, index=False)
  dest = tmp_dir_path + '/' + new_file
  shutil.move(data_dir_path + '/' + new_file, dest)
  print("SUCCESS: File moved into tmp folder")
else:
  print("ERR: SKIPPING, duplicate file detected" + new_file)