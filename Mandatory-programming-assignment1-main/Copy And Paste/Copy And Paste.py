import json
import csv

with open("incident.json", "r") as incident:
    incident_report = json.load(incident)
    print(incident_report)

with open("domains.csv", "w", newline="") as domains:
    domains_writer = csv.writer(domains)
    domains_writer = csv.writer(domains, quoting=csv.QUOTE_ALL)
    domains_writer.writerow(["alertId", "machineId", "firstActivity", "domains"])

    for domains_loop in incident_report["alerts"]:
        alertid = domains_loop["alertId"]
        machineId = domains_loop["machineId"]
        firstactivity = domains_loop["firstActivity"]
        domains_list = domains_loop["entities"]["domains"]

        for incident_domains in domains_list:
            domains_writer.writerow([alertid,machineId,firstactivity,incident_domains])

with open("filehashes.csv", "w", newline="") as filehash: 
    hash_writer = csv.writer(filehash)
    hash_writer = csv.writer(filehash, quoting=csv.QUOTE_ALL)
    hash_writer.writerow(["alertId", "machineId", "firstActivity", "fileHashes"])

    for hash_loop in incident_report["alerts"]:
        alertid = hash_loop["alertId"]
        machineId = hash_loop["machineId"]
        firstactivity = hash_loop["firstActivity"]
        hash_list = hash_loop["entities"]["fileHashes"]

        for incident_hash in hash_list: 
            hash_writer.writerow([alertid,machineId,firstactivity,incident_hash])

with open("ips.csv", "w", newline="") as ips:
    ips_writer = csv.writer(ips)
    ips_writer = csv.writer(ips, quoting=csv.QUOTE_ALL)
    ips_writer.writerow(["alertId", "machineId", "firstActivity", "ips"])

    for ips_loop in incident_report["alerts"]:
        alertid = ips_loop["alertId"]
        machineId = ips_loop["machineId"]
        firstactivity = ips_loop["firstActivity"]
        ips_list = ips_loop["entities"]["ips"]

        for incident_ips in ips_list:
            ips_writer.writerow([alertid,machineId,firstactivity,incident_ips])

with open("processes.csv", "w", newline="") as processes: 
    processes_writer = csv.writer(processes)
    processes_writer = csv.writer(processes, quoting=csv.QUOTE_ALL)
    processes_writer.writerow(["alertId", "machineId", "firstActivity", "processes"])

    for processes_loop in incident_report["alerts"]:
        alertid = processes_loop["alertId"]
        machineId = processes_loop["machineId"]
        firstactivity = processes_loop["firstActivity"]
        processes_list = processes_loop["entities"]["processes"]

        for incident_processes in processes_list:
            processes_writer.writerow([alertid,machineId,firstactivity,processes_list])