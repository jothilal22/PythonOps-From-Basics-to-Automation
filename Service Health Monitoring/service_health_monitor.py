import psutil
import time
import csv

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

LOG_FILE = system_health_log.csv

def get_system_health():
    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
    }

def log_system_health(data):
    file_exists = False
    try:
        with open(LOG_FILE, "r") as f:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(LOG_FILE, "a", newline) as f:
        writer = csv.DictReader(f, fieldnames = data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)
    

def check_alerts(data):
    if data["cpu_usage"] > CPU_THRESHOLD:
        print(f"High CPU usage Alert: {data['cpu_usage']}%")
    if data["memory_usage"] > MEMORY_THRESHOLD:
        print(f"High Memory usage Alert: {data['memory_usage']}%")
    if data["disk_usage"] > DISK_THRESHOLD:
        print(f"High Disk usage Alert: {data['disk_usage']}%")
    

if __name__ == "__main__":
    print("Starting Server Health Monitoring")
    while True:
        system_data = get_system_health()
        log_system_health(system_data)
        check_alerts(system_data)
        time.sleep(60)


    
