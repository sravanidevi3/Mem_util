import paramiko
import csv
import os
import sys
import traceback

username = sys.argv[1]
password = sys.argv[2]
csvpath = sys.argv[3]
reportpath = sys.argv[4]

csv_fullpath = os.path.join(csvpath , "servers.csv")
report_fullpath = os.path.join(reportpath , "Helathcheck.csv")

def mem_utility(ip, username, password, script):
    #establish a connection
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname= ip, username= username, password= password)

    stdin,stdout,stderr = client.exec_command(script)

    return stdout.readlines()


with open(csv_fullpath ,'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file , delimiter=',')
    
    results = []

    for row in csv_reader:
        ip = row[0]
        port = 22
        hostname = ip

        script = "df -h"

        try:

            out_result = mem_utility(hostname , username, password, script)
            disc_util = out_result[1].strip()
            results.append([ip , disc_util])

        except Exception as e:
            print(f"This the exception occurred on {ip} as {e} ")
    
with open(report_fullpath , 'w' , newline= '', encoding='utf-8-sig') as report_file:
    csv_writer = csv.writer(report_file)
    csv_writer.writerow(["ip" ,"utilization"])
    csv_writer.writerows(results)


print(" Health check report is prepared")
    
