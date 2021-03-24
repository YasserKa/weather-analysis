import glob
import os

# Type in the folder- and filename to read the files
folder_name = "TG"
file_names = "TG_*.txt"

# Fetch the folder with the specific data files
abs_path = os.path.abspath(folder_name) # Replace the string here with your target folder 

# Get all the files in the folder
txt_files = glob.glob(abs_path+"\\"+file_names)
print((f'The absoule path to the target folder: {abs_path} \n\n')+
        (f'Number of data files in the folder: {len(txt_files)}'))

folder = "mean_temp_preprocessed"
path = abs_path.replace(folder_name,"")+folder+"\\"

try:
    os.mkdir(path)
except:
    pass

for i in range(len(txt_files)):
    txt_file = open(txt_files[i], encoding = "utf8")
    TG = open((f"{path}mt{i+0}.txt"), "w")
    dataset = txt_file.read().split("\n")
    for j in range(len(dataset)):
        if j > 19:
            TG.write("%s\n" % dataset[j])
    print(f"\rNumber of preprocessed text files: {i+1}", end='', flush=True)
