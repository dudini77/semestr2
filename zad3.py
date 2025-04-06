import zipfile
import os 
import datetime
def backup(input, output):
    output= f"{output}_kopia_{datetime.date.today()}.zip"
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_BZIP2) as zip:
        for root, dirs, files in os.walk(input):
            for file in files:
                path_file = os.path.join(root, file)
                zip.write(path_file, os.path.relpath(path_file, input)) 
backup("dobackup", "kopia")