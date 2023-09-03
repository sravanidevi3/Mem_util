import os
import csv
import paramiko
import traceback
import sys

username = sys.argv[1]
password = sys.argv[2]
csvpath = sys.argv[3]
reportpath = sys.argv[4]

csv_fullpath = os.path.join(csvpath , "server.csv")
report_fullpath = os.path.join(reportpath , "reportfull.csv")

def mem_util(ip , username , password , script):
    #Establishing connection.
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname = ip , username = username , password = password)

    stdin,stdout,stderr = client.exec_command(script)

    return stdout.readlines()

with open(csv_fullpath , 'r' , encoding= "utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file , delimiter=',')

    results = []

    for row in csv_reader:
        ip = row[0]
        port = 22
        hostname = ip

        script = "df -h"
        try:
            out_result = mem_util(ip , username , password , script)
            mem_util = results[2].strip()
            results.append(ip , mem_util)
        except Exception as e:
            print ("an errro occurred while authenticates as {e}")

with open (report_fullpath , 'w', newline= '' , encoding="utf-8-sig") as reportfile:
    csv_writer = csv.writer(reportfile)
    csv_writer.writerow("ip", "utilization")
    csv_writer.writerows(results)


print("health check is created")
