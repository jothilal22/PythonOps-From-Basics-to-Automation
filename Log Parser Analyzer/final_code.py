import re
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Sample log file path (update this path)
LOG_FILE = "server_logs.log"

# Regex to parse log lines
LOG_PATTERN = r'(?P<ip>\S+) - - \[(?P<timestamp>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<size>\d+)'

def parse_logs(file_path):
    log_entries = []
    
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(LOG_PATTERN, line)
            if match:
                log_entries.append(match.groupdict())
    
    return pd.DataFrame(log_entries)

def analyze_logs(df):
    print("\nTop 10 Requested URLs:")
    print(df['url'].value_counts().head(10))
    
    print("\nHTTP Status Code Distribution:")
    print(df['status'].value_counts())
    
    # Identify top error sources
    error_ips = df[df['status'].astype(int) >= 400]['ip'].value_counts().head(10)
    print("\nTop 10 IPs Causing Errors:")
    print(error_ips)

def plot_traffic(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], format="%d/%b/%Y:%H:%M:%S %z")
    df.set_index('timestamp', inplace=True)
    traffic = df.resample('1H').size()
    
    plt.figure(figsize=(10, 5))
    plt.plot(traffic, marker='o', linestyle='-')
    plt.title("Hourly Traffic Trend")
    plt.xlabel("Time")
    plt.ylabel("Number of Requests")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

def print_raw_logs(file_path):
    print("\nRaw Log Data:")
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())

def extract_log_data(file_path):
    print("\nExtracted Log Data:")
    with open(file_path, "r") as file:
        for line in file:
            match = re.match(LOG_PATTERN, line)
            if match:
                print(match.groupdict())

if __name__ == "__main__":
    print_raw_logs(LOG_FILE)
    extract_log_data(LOG_FILE)
    df = parse_logs(LOG_FILE)
    if not df.empty:
        analyze_logs(df)
        plot_traffic(df)
    else:
        print("No valid log entries found!")




# Output will look like this 
# Raw Log Data:
# 192.168.1.1 - - [10/Mar/2024:14:23:45 +0000] "GET /index.html HTTP/1.1" 200 1024
# 192.168.1.2 - - [10/Mar/2024:14:24:05 +0000] "POST /login HTTP/1.1" 403 512
# 192.168.1.3 - - [10/Mar/2024:14:25:15 +0000] "GET /dashboard HTTP/1.1" 500 2048

# Extracted Log Data:
# {'ip': '192.168.1.1', 'timestamp': '10/Mar/2024:14:23:45 +0000', 'method': 'GET', 'url': '/index.html', 'status': '200', 'size': '1024'}
# {'ip': '192.168.1.2', 'timestamp': '10/Mar/2024:14:24:05 +0000', 'method': 'POST', 'url': '/login', 'status': '403', 'size': '512'}
# {'ip': '192.168.1.3', 'timestamp': '10/Mar/2024:14:25:15 +0000', 'method': 'GET', 'url': '/dashboard', 'status': '500', 'size': '2048'}

# Top 10 Requested URLs:
# url
# /index.html    1
# /login         1
# /dashboard     1
# Name: count, dtype: int64

# HTTP Status Code Distribution:
# status
# 200    1
# 403    1
# 500    1
# Name: count, dtype: int64

# Top 10 IPs Causing Errors:
# ip
# 192.168.1.2    1
# 192.168.1.3    1