import os
import re
import taglib

image_ext=["png","jpg","jpeg"]
audio_ext=["mp3","flac","m4a","ogg","opus","ape"]

def normPath(path:str)->str:
    return os.path.abspath(os.path.expanduser(os.path.expandvars(path)))

def isMusicDir(path : str)->bool:
    has_image_file=False
    has_audio_file=False
    if os.path.isdir(path):
        has_image_file=any("."+ext in filename for filename in os.listdir(path) for ext in image_ext)
        has_audio_file=any("."+ext in filename for filename in os.listdir(path) for ext in audio_ext)
        return has_audio_file and has_image_file
    else:
        return False
    
def normDirName(path:str):
    def getArbitraryAudioFile(path:str)->taglib.File:
        for filename in os.listdir(path):
            for ext in audio_ext:
                if "."+ext in filename:
                    return taglib.File(os.path.join(path,filename))
    parent_dir_path=os.path.abspath(os.path.join(path, os.pardir))
    arbitrary_audio_file=getArbitraryAudioFile(path).tags
    new_dir_path=os.path.join(parent_dir_path,arbitrary_audio_file["ALBUMARTIST"][0]+" - "+arbitrary_audio_file["ALBUM"][0])
    os.replace(path,new_dir_path)
    


    
            

    

