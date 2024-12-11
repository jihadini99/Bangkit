  #!/bin/bash
> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for file in $files; do
  if [ -e "/home/student-02-df9516af8462"$file ]; then
    echo "/home/student-02-df9516af8462"$file >> oldFiles.txt;
  fi
done


#!/usr/bin/env python3
import sys
import subprocess

files = open(sys.argv[1], 'r')
for i in files.readlines():
  old_name = line.strip()
  new_name = old_name.replace("jane","jdoe")
  subprocess.run(["mv"], old_name, new_name)
f.close()
