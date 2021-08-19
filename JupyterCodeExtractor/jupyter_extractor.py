# jupyter code exporter
import tkinter as tk
from tkinter import filedialog
import json
import os
from pathlib import Path

# select files from explorer
root = tk.Tk()
root.withdraw()

files = filedialog.askopenfilenames()
working_dir = Path(__file__).resolve().parent

# checking if dir exist
if not working_dir.joinpath('out').is_dir():
    os.mkdir(str(working_dir) + '\\out')
out_dir = Path(__file__).resolve().parent.joinpath('out')

for file in files:
    # file name without extension.
    file_name = ".".join(str(os.path.basename(file)).split('.')[:-1])
    with open(file, 'r') as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError as ex:
            print(ex)
        json_file.close()
    with open(out_dir.joinpath(file_name + ".py"), 'w') as python_file:
        i = 0
        for json in data['cells']:
            try:
                if json["cell_type"] == 'code':
                    i += 1
                    for line in json['source']:
                        python_file.write(line)
                    python_file.write("\n#####>>>>   end of code number %d <<<<####\n" % i)
            except Exception as ex:
                print(ex)
