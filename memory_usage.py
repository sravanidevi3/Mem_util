import os
import paramiko
import traceback
import csv
import sys
from configparser import ConfigParser

username = sys.argv[1]   
password = sys.argv[2]
csvpath = sys.argv[3]
reportpath = sys.argv[4]

csv_fullpath = os.path.join(csvpath, "servers.csv")
report_fullpath = os.path.join(reportpath, "Healthcheck.csv")

def mem_utility(ip: str, username: str, password: str, script: str):
    # Establish SSH connection
    print(f"Attempting SSH Connection to {ip}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(script)
    return stdout.readlines()

with open(csv_fullpath, 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Create a list to store the results
    results = []

    for row in csv_reader:
        ip = row[0]
        port = 22
        hostname = ip

        script = "free -m"

        try:
            out_result = mem_utility(ip, username, password, script)

            # Extract relevant information from the output
            disk_util = out_result[1].strip()

            results.append([ip, disk_util])

        except Exception as e:
            print(f"An error occurred for {ip}: {e}")

# Write the results to the output CSV file
with open(report_fullpath, 'w', newline='', encoding='utf-8-sig') as report_file:
    csv_writer = csv.writer(report_file)
    csv_writer.writerow(['IP', 'Disk Utilization'])
    csv_writer.writerows(results)

print("Healthcheck completed and results saved in Healthcheck.csv")
