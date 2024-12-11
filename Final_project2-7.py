#!/usr/bin/env python3

import re
import csv
import sys
import operator

per_user = {}
error = {}

logfile = 'syslog.log'

info_pattern = r"ticky: INFO: \((\.+)\)"
error_pattern = r"ticky: ERROR: ([\w\s']*) \((\.+)\)" 

with open(logfile, 'r') as files:
    for line in files():
       per_user_message = re.search(info_pattern, line)
       error_message = re.search(error_pattern, line)



per_user_sorted = sorted(per_user.items())
error_sorted = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
return per_user_sorted, error_sorted

with open('error_message.csv', "w+") as error_output:
    writer = csv.writer(error_output)
    writer.writerow(["Error", "Count"])
    writer.writerows(error_message_sorted)
with open('user_statistics.csv','w+') as users_output:
    writer = csv.writer(users_output)
    writer.writerow(["Username", "INFO", "ERROR"])
    for i in per_user:

        writer.writerows()
