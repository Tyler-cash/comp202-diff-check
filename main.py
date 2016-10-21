import os

import shutil

current_dir = os.getcwd()
stage = "stage1"
dir_name = "run"

# Instantiates directory
run_dir = os.path.join(current_dir, stage, dir_name)

# Deletes dir if it exists
if os.path.exists(run_dir):
    os.removedirs(run_dir)
os.makedirs(run_dir)
print("Directory \"" + dir_name + "\" created")

