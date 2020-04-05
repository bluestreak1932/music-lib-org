import subprocess
import music_dir_tools

path=music_dir_tools.normPath("/home/brocolio/Music/Lossless/revisado/(2013) Präparat")
print(music_dir_tools.isMusicDir(path))