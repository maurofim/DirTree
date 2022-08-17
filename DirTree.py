#!/usr/bin/env python3

import os
import re
import shutil

def get_parent_dir(file_path):
    r_path = '\/[\w]*$'
    current_file = re.search(r_path, file_path).group()
    parent_dir_path = file_path.replace(current_file,'')
    return (parent_dir_path, current_file)

path = str(input('enter path directory: '))
r_directories = '\/[\w ]*'

with open ('DirTree_info.txt', 'w') as f:
    for root, dirs, subdirs in os.walk(path):
        for dir in dirs, subdirs:
            dir_path_end = root.replace(get_parent_dir(path)[0],'')
            dir_list = re.findall(r_directories, dir_path_end)
            cleaned_path = ''
            for name in dir_list:
                name = name + '.copy'
                cleaned_path += name
                if os.path.exists(get_parent_dir(path)[0] + cleaned_path):
                    pass
                else:
                    os.mkdir(get_parent_dir(path)[0] + cleaned_path)
                    f.write(root + '\n')
