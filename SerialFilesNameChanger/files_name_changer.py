from tkinter import filedialog
import tkinter as tk
from pathlib import Path
import os
import re

# select files from explorer
root  = tk.Tk()
root.withdraw() 
files = filedialog.askopenfilenames()

working_dir = Path(files[0]).resolve().parent


# get template file name
print ("Enter template name instead of episod number use {}.\n"
       "Remeber don't type file extention(suffix)\n"
       "For example if your file name is One.Pice.245.[480p].mkv \n"
       "you should type for example one_pice_{}_480p as you can see \n"
       "there is no extention mkv.") # One.pice.epi%

template_name = input("Enter tmeplate: ")
while template_name.count("{}") != 1:
    print ("you did't use '{}' or used more than one time. Try again")
    template_name = input("Enter template: ")

# get number of digit of epi nubmer for regex
print()
digit_number = None
while digit_number == None:
    try:
        x = int(input("Enter digit number: "))
        if x <= 0 :
            print(x)
            raise BaseException()
        digit_number = x
    except Exception as ex:
        print("input number not a posetive integer")
    
regex = "\d{" + str(digit_number) + "}"
    
for file in files:
    # get file name and extention
    file_name = os.path.basename(file)
    file_extention = os.path.splitext(file)[1]

    # find epi number
    index_epi_num = re.search(regex, file_name)
    if index_epi_num:
        index_epi_num = index_epi_num.start()
        epi_num = int(file_name[ index_epi_num : index_epi_num+digit_number])
        os.rename(file,working_dir.joinpath(template_name.format(epi_num) + file_extention))
        
    else:
        print (r"file with name {file_name} not include number with {digit_number} digits" )
