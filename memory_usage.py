import sys
import os
import csv
import paramiko
import traceback

username = sys.argv[1]
password = sys.argv[2]
csvpath = sys.argv[3]
reportpath = sys.argv[4]

csv_path = os.path.join(csvpath,"servers.csv")
report_path = os.path.join(reportpath,"Healthcheck.csv")

def mem_util(ip: str , username: str , password: str , script: str):
    print("Attempting ssh connection")
    #Establish ssh connection
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip , username=username , password=password)

    stdin,stdout,stderr=client.exec_command("script")
    return stdout.readlines()

with open(csv_path , 'r' , encoding="utf-8-sig")as csv_file:
    csv_reader = csv.reader(csv_file , delimiter='')

    results=[]
    for row in csv_reader:
        ip = results()
        port = 22
        hostname = ip
        script = "free -m"

        try:
            out_results=mem_util([ip,username,password,script])
            mem_util=out_results[1].strip()
            results.append([ip , mem_util])

        except Exception as e:
            print("An error occured for{ip} as {e}")

with open(report_path , 'w', newline = '' ,encoding="utf-8-sig")as report_file:
    csv_writer=csv.writer(report_file)
    csv_writer.writerow(results)
    csv_writer.writerows(["IP","Mem_util"])

print("Healthcheck is ssaved in Healthcheck.csv")


