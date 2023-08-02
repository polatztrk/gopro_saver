import os 
import time
import inquirer
import shutil

paths_to_try=[
    '/media/romer/1737-6E41/DCIM/100GOPRO',
    '/media/romer/6361-3930/DCIM/100GOPRO',
    '/media/romer/3235-6530/DCIM/100GOPRO'
]

questions = [inquirer.Checkbox(
    'cam_id',
    message="Please choose which device is this?(Space for chossing and then Enter for continuing)",
    choices=['Isometric-Surface','Bottom-Underwater','Isometric-Underwater'],
)]
answers = inquirer.prompt(questions) 
if not answers:
    print("\033[33mYou dont select a device\033[0m")
    
    
cameraId=answers['cam_id'][0]
#dir = '/media/romer/1737-6E41/DCIM/100GOPRO'
try_count=0
for dir in paths_to_try:
    if os.path.exists(dir):
        for file in os.listdir(dir):
            old_filepath = os.path.join(dir, file)
            date = time.ctime(os.path.getctime(old_filepath))
            date2 = date.replace(" ", "--").replace(":", "-") +cameraId+ '.MP4'
            new_filepath = os.path.join(dir, date2)
            
            os.rename(old_filepath, new_filepath)
            date_3=cameraId+'/'+date2
            dest_filepath= os.path.join('/home/romer/Desktop/',date_3)
            shutil.copy2(new_filepath,dest_filepath)
        print(f"\033[32mAll files are renamed and copied to the destination.\033[0m")
    else:
        print(f"\033[33m[Warning] Path does not exist: {dir}. Trying next path from the list...\033[0m")
        try_count = try_count+1
        if try_count==3:
            print("\033[31mThere is no device to connect\033[0m")

