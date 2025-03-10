#Store log data using python list 
import re

logs_file = "server_logs.log"

LOG_PATTERN = r'(?P<ip>\S+) - - \[(?P<timestamp>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+)'

log_entries = []

with open(logs_file, "r") as file:
    for line in file:
        match = re.match(LOG_PATTERN, line)
        if match:
            log_entries.append(match.groupdict())
print(log_entries)

# Output will look like this 
# [{'ip': '192.168.1.1', 'timestamp': '10/Mar/2024:14:23:45 +0000', 'method': 'GET', 'url': '/index.html', 'status': '200', 'size': '1024'}, {'ip': '192.168.1.2', 'timestamp': '10/Mar/2024:14:24:05 +0000', 'method': 'POST', 'url': '/login', 'status': '403', 'size': '512'}, {'ip': '192.168.1.3', 'timestamp': '10/Mar/2024:14:25:15 +0000', 'method': 'GET', 'url': '/dashboard', 'status': '500', 'size': '2048'}]