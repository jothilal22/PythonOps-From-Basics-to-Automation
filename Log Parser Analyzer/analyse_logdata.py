import re
import pandas as pd
from collections import Counter

log_files = "server_logs.log"

LOG_PATTERN = r'(?P<ip>\S+) - - \[(?P<timestamp>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+)'

def parse_logs(file_path):
    log_entries = []
    
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(LOG_PATTERN, line)
            if match:
                log_entries.append(match.groupdict())

    return pd.DataFrame(log_entries)

df = parse_logs(log_files)

if df.empty:
    print("No valid log entries found!")
    exit()
status_counts = Counter(df['status'])
print("\n Status code Distribution")
for status, count in status_counts.items():
    print(f"{status}: {count} times")

URLs = Counter(df['url'])
print("\n URL Distribution")
for url, count in URLs.items():
    print(f"{url}: {count} times")