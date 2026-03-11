import json
import csv

#This opens and reads the incident.json file
with open("incident.json", "r") as incident:
    incident_report = json.load(incident)
    print(incident_report)

#writes the csv files so we can convert the json data to csv
with open("domains.csv", "w", newline="") as domains,\
     open("fileHash.csv", "w", newline="") as fileHashes,\
     open("ips.csv", "w", newline="") as ips,\
     open("processes.csv", "w", newline="") as processes:

    domains_writer = csv.writer(domains, quoting=csv.QUOTE_ALL)
    fileHashes_writer = csv.writer(fileHashes, quoting=csv.QUOTE_ALL)
    ips_writer = csv.writer(ips, quoting=csv.QUOTE_ALL)
    processes_writer = csv.writer(processes, quoting=csv.QUOTE_ALL)
    
    
    #Headers
    domains_writer.writerow(["alertId", "machineId", "firstActivity", "domains"])
    fileHashes_writer.writerow(["alertId", "machineId", "firstActivity", "fileHashes"])
    ips_writer.writerow(["alertId", "machineId", "firstActivity", "ips"])
    processes_writer.writerow(["alertId", "machineId", "firstActivity", "processses"])

    for alerts in incident_report["alerts"]:
        alertId = alerts["alertId"]
        machineId = alerts["machineId"]
        firstActivity = alerts["firstActivity"]
        domains_list = alerts["entities"]["domains"]
        fileHash_list = alerts["entities"]["fileHashes"]
        ips_list = alerts["entities"]["ips"]
        processes_list = alerts["entities"]["processes"]
    

        for domain in domains_list:
            domains_writer.writerow([alertId, machineId, firstActivity, domain])
        
        for fileHash in fileHash_list:
            fileHashes_writer.writerow([alertId, machineId, firstActivity, fileHash])
        
        for ips in ips_list:
            ips_writer.writerow([alertId, machineId, firstActivity, ips])
        
        for processes in processes_list:
            processes_writer.writerow([alertId, machineId, firstActivity, processes])


 