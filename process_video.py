#converts the  videos to mp3
import os
import subprocess
files=os.listdir('videos')
print(files)
for file in files:
    
    tutorial_number = file.split(".")[0]   
    print(tutorial_number,file)
    subprocess.run(['ffmpeg','-i',f'videos/{file}',f'audios/{tutorial_number}_{file}.mp3'])
