#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool

def run(src):
    dest = "./data/prod_backup/"
    subprocess.call(["rsync", "-arq", src, dest])
    print("Move from {} to {}".format(src, dest))

if __name__ == "__main__":
    files_include = list()
    list_of_files = os.listdir("./data/prod/")
    for root in list_of_files:
        path = os.path.join("./data/prod/", root)
        if os.path.isdir(path):
            files_include.append(path)
    p = Pool(len(files_include))
    p.map(run, files_include)

