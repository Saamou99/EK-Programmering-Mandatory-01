# This allows Python to read and work with JSON files
import json
# This allows Python to create and write CSV files
import csv

# ---------------------------
# READ JSON FILE
# ---------------------------

# Open the incident.json file in read mode ("r")
# "with" ensures the file automatically closes after the block finishes
with open("incident.json", "r") as incident:

    # Convert the JSON data into a Python dictionary
    incident_report = json.load(incident)

    # Print the entire JSON structure (useful for debugging)
    print(incident_report)

# ---------------------------
# CREATE CSV FILES
# ---------------------------

# Open four CSV files in write mode ("w")
# newline="" prevents blank lines between rows (important for Windows)
# Each file will store a different type of data from the JSON file

with open("domains.csv", "w", newline="") as domains,\
     open("fileHash.csv", "w", newline="") as fileHashes,\
     open("ips.csv", "w", newline="") as ips,\
     open("processes.csv", "w", newline="") as processes:

    # Create CSV writer objects for each file
    # csv.writer() allows us to write rows into the CSV files
    # quoting=csv.QUOTE_ALL ensures all values are wrapped in quotes
    domains_writer = csv.writer(domains, quoting=csv.QUOTE_ALL)
    fileHashes_writer = csv.writer(fileHashes, quoting=csv.QUOTE_ALL)
    ips_writer = csv.writer(ips, quoting=csv.QUOTE_ALL)
    processes_writer = csv.writer(processes, quoting=csv.QUOTE_ALL)
    
    # ---------------------------
    # WRITE HEADER ROWS
    # ---------------------------

    # These are the column names that will appear at the top of each CSV file
    domains_writer.writerow(["alertId", "machineId", "firstActivity", "domains"])
    fileHashes_writer.writerow(["alertId", "machineId", "firstActivity", "fileHashes"])
    ips_writer.writerow(["alertId", "machineId", "firstActivity", "ips"])
    processes_writer.writerow(["alertId", "machineId", "firstActivity", "processes"])

    # ---------------------------
    # LOOP THROUGH ALERTS
    # ---------------------------

    # The JSON file contains a list of alerts
    # This loop goes through each alert one by one
    for alerts in incident_report["alerts"]:

        # Extract basic information from each alert
        alertId = alerts["alertId"]
        machineId = alerts["machineId"]
        firstActivity = alerts["firstActivity"]

        # Extract lists of entities from the JSON structure
        domains_list = alerts["entities"]["domains"]
        fileHash_list = alerts["entities"]["fileHashes"]
        ips_list = alerts["entities"]["ips"]
        processes_list = alerts["entities"]["processes"]

        # ---------------------------
        # WRITE DOMAIN DATA
        # ---------------------------

        # Loop through each domain in the domains list
        for domain in domains_list:

            # Write one row to domains.csv
            domains_writer.writerow([alertId, machineId, firstActivity, domain])
        
        # ---------------------------
        # WRITE FILE HASH DATA
        # ---------------------------

        # Loop through each file hash
        for fileHash in fileHash_list:

            # Write one row to fileHash.csv
            fileHashes_writer.writerow([alertId, machineId, firstActivity, fileHash])

        # ---------------------------
        # WRITE IP ADDRESS DATA
        # ---------------------------

        # Loop through each IP address
        for ips in ips_list:

            # Write one row to ips.csv
            ips_writer.writerow([alertId, machineId, firstActivity, ips])

        # ---------------------------
        # WRITE PROCESS DATA
        # ---------------------------

        # Loop through each process name
        for processes in processes_list:

            # Write one row to processes.csv
            processes_writer.writerow([alertId, machineId, firstActivity, processes])