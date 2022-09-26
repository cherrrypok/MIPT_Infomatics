import shutil
import os

shutil.unpack_archive("main.zip")
answer = []

for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if '.py' in file and current_dir not in answer:
            answer.append(current_dir)

with open("answer_file_3.txt", 'w') as answer_file:
    answer.sort()
    answer_file.write('\n'.join(answer))



