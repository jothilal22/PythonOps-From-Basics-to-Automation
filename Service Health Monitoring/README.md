# Server Health Monitor  

## 📌 Overview  
The **Server Health Monitor** is a Python script that continuously tracks **CPU usage, memory usage, and disk space**. It logs the data to a CSV file and triggers alerts if usage exceeds predefined thresholds.

## 🚀 Features  
- ✅ **Monitors CPU, memory, and disk usage** in real-time  
- ✅ **Logs system metrics** to `system_health_log.csv`  
- ✅ **Alerts when usage exceeds set thresholds**  
- ✅ **Runs continuously with periodic updates**  

## 📊 Example Output  
```sh
Starting Server Health Monitoring...
{'timestamp': '2024-03-10 14:23:45', 'cpu_usage': 45.5, 'memory_usage': 65.3, 'disk_usage': 70.1}
{'timestamp': '2024-03-10 14:23:50', 'cpu_usage': 82.1, 'memory_usage': 85.2, 'disk_usage': 71.5}
⚠️ High CPU Usage Alert: 82.1%
⚠️ High Memory Usage Alert: 85.2%
{'timestamp': '2024-03-10 14:23:55', 'cpu_usage': 60.5, 'memory_usage': 68.3, 'disk_usage': 72.0}

timestamp,cpu_usage,memory_usage,disk_usage
2024-03-10 14:23:45,45.5,65.3,70.1
2024-03-10 14:23:50,82.1,85.2,71.5
2024-03-10 14:23:55,60.5,68.3,72.0
