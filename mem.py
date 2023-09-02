import sys
import os
import paramiko
import traceback
import csv

username = sys.argv[1]
password = sys.argv[2]
csvpath = sys.argv[3]
reportpath = sys.argv[4]


csv_path = os.path.join(csvpath,"servers.csv")
report_path = os.path.join(reportpath,"Healthcheck.csv")


with open(csv_path , 'r' , encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file , delimiter=',')

#store the results in list format
results = []

for row in csv_reader:
    ip = row[0]
    port = 22
    hostname = ip

    script = "free -m"

    try:
        out_results = mem_util([ip , username , password , script])
        mem_util = out_results[1].strip()
        results.append([ip,mem_util])

    except Exception as e:
        print("An error has occured for {ip} as {e}")


with open(report_path , 'w' , newline = '' , encoding = 'utf-8-sig') as report_file:
    csv_writer = csv.writer(report_file)
    csv_writer.row(['IP' , 'Mem_util'])
    csv_writer.row(results)

def mem_util(ip:str , username:str , password:str , script:str):
    #Establish SSH Connection
    print("Attemping ssh connection for {ip}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect([hostname , username , password])

    stdin,stdout,stderr=client.exec_command(script)
    return stdout.readlines()

print("Healthcheck is saved Healthcheck.csv")

