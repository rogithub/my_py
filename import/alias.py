#!/usr/bin/env python3
"""Imports aliases on linux"""
import sys
import os
import re

def printHelp():
    print("usage:")
    print("ptyhon3 alias.py <path_to_alias_file> <path_to_functions_folder | default: ~/.config/fish/functions/ >")

def create_fish_alias_func(alias, dest_dir):
    m = re.search("(=[\"'])(.*)([\"'])", alias)
    alias_cmd = m.group(2)
    alias_name = alias[6:].split("=")[0]
    file_name = alias_name + ".fish"
    file_name = os.path.join(dest_dir, file_name)
    if (os.path.isfile(file_name)):
        os.remove(file_name)

    cmd = "function {} \n    {} $argv\nend".format(alias_name, alias_cmd)
    with open(file_name, 'w+') as f:
        f.write(cmd)
    
    
def file_to_fish_shell(file_path, dest_dir):
    with open(file_path) as fp:
        for cnt, line in enumerate(fp):
            if (line[0:5] == 'alias'):
                create_fish_alias_func(line, dest_dir)

def main(file_path, dest_directory):
    file_to_fish_shell(file_path, dest_directory)
    
if __name__ == "__main__":

    directory = "~/.config/fish/functions/"
    if (len(sys.argv) > 2 and sys.argv[2]):
        directory = sys.argv[2]
        print(directory)

    file_path = ''
    if (sys.argv[1]):
        file_path = sys.argv[1]

    has_error = False
    
    if not os.path.exists(directory):
        print('Destination directory not found: "{}"'.format(directory))
        has_error = True
              
    if not os.path.isfile(file_path):
        print('File not found: "{}"'.format(file_path))
        has_error = True

    if has_error:
        printHelp()
    else:
        main(file_path, directory)

        
