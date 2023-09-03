import csv
import os
import traceback
import sys
import paramiko

username = sys.argv[1]
password = sys.argv[2]
csvpath = sys.argv[3]
reportpath = sys.argv[4]

csv_path = os.path.join(csvpath,"servers.csv")
report_path = os.path.join(reportpath,"Healthcheck.csv")

def mem_utility(ip:str , username:str, password:str, script:str):
    print(f"Attempting ssh connection")
    #Establishing ssh connection
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip , username=username , password=password)
    
    stdin,stdout,stderr=client.exec_command(script)
    return stderr.readlines()

with open(csv_path , 'r' , encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file , delimiter=',')

    results=[]
    for row in csv_reader:
        ip = row[0]
        hostname = ip
        port = 22

        script = "free -m"


        try:
            out_results = mem_utility(ip , username , password , script)
            mem_util = out_results[1].strip()
            results.append([ip,mem_utility])

        except Exception as e:
            print(f"An error has occured as {e}") 


with open(report_path , 'w' , newline = '' ,encoding = 'utf-8-sig') as report_file:
    csv_writer = csv.writer(report_file)
    csv_writer.writerows(results)
    csv_writer.writerow(["IP" , "MEM_UTILITY"])

print("Healthcheck is saved in healthcheck.csv")


