#!/usr/bin/env python3

import re
import csv
import sys
import operator

    # logfile = 'syslog.log'
    # info_pattern = r"ticky: INFO: \((\.+)\)"   
    # error_pattern = r"ticky: ERROR: ([\w\s']*) \((\.+)\)" 

def stat(logfile):
    per_user = {}
    error = {}

    with open(logfile, 'r') as file:
        for line in file.readlines():
            pattern = r"(INFO|ERROR) ([\w']*) [\[\]\d# ]*\(([\w\.]*)\)$"
            # ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$"
            result = re.search(pattern, line)
            type = result.group(1)
            user = result.group(2)
            message = result.group(3)

            if type == "ERROR":
                if message in error:
                    error[message] = error[message]+1
                else:
                    error[message] = 1
            
            if user in per_user:
                if type == "ERROR":
                    per_user[user][type] = per_user[user][type] + 1
                elif type == "INFO":
                    per_user[user][type] = per_user[user][type] + 1
            else:
                if type == "ERROR":
                    per_user[user] = {"ERROR": 1, "INFO": 0}
                elif type == "INFO":
                    per_user[user] = {"ERROR": 0, "INFO": 1}
    
    per_user_sorted = sorted(per_user.items())
    error_sorted = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
    return (per_user_sorted, error_sorted)

def csv_file(per_user, error):
    with open(sys.argv[1]+'/user_statistics.csv','w') as user_csv:
        writer = csv.writer(user_csv)
        writer.writerow(["Username", "INFO", "ERROR"])
        for item in per_user:
            user, type = item
            line = [user, type["INFO"], type["ERROR"]]
            writer.writerow(line)

    with open(sys.argv[1]+ '/error_message.csv', 'w') as error_csv:
        writer = csv.writer(error_csv)
        writer.writerow(["Error", "Count"])
        writer.writerows(error)

if __name__ == "__main__":
    logfile = sys.argv[1]
    per_user, error = stat(logfile)
    csv_file(per_user, error)
