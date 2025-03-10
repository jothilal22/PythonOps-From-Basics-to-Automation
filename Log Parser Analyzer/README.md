# Log Parser Analyzer

## Overview
This project is a **Log Parser & Analyzer** that extracts useful insights from server logs. It processes raw logs, extracts relevant data, analyzes HTTP status codes, identifies frequent requests, and visualizes traffic trends.

---

## **Tasks**

### **1. Print Raw Logs**
**Function:** `print_raw_logs(file_path)`  
✅ Reads and prints each line of the log file as raw text.  

### **2. Extract Structured Log Data**
**Function:** `extract_log_data(file_path)`  
✅ Uses **Regular Expressions (Regex)** to extract key fields like IP, Timestamp, Method, URL, Status Code, and Size.

### **3. Parse Logs into DataFrame**
**Function:** `parse_logs(file_path)`  
✅ Converts extracted log data into a **Pandas DataFrame** for easy analysis.

### **4. Analyze Log Data**
**Function:** `analyze_logs(df)`  
✅ Identifies:
   - **Top 10 Requested URLs**
   - **HTTP Status Code Distribution**
   - **Top 10 IPs causing errors**

### **5. Visualize Traffic Trends**
**Function:** `plot_traffic(df)`  
✅ Converts timestamps into **datetime format** and generates a traffic trend graph using **Matplotlib**.

---

## **How to Run**
1. **Ensure Dependencies are Installed**:
   ```bash
   pip install pandas matplotlib


## **Expected Output**

### **Raw Log Data:**
192.168.1.1 - - [10/Mar/2024:14:23:45 +0000] "GET /index.html HTTP/1.1" 200 1024 192.168.1.2 - - [10/Mar/2024:14:24:05 +0000] "POST /login HTTP/1.1" 403 512 192.168.1.3 - - [10/Mar/2024:14:25:15 +0000] "GET /dashboard HTTP/1.1" 500 2048

### **Extracted Log Data:**
{'ip': '192.168.1.1', 'timestamp': '10/Mar/2024:14:23:45 +0000', 'method': 'GET', 'url': '/index.html', 'status': '200', 'size': '1024'} {'ip': '192.168.1.2', 'timestamp': '10/Mar/2024:14:24:05 +0000', 'method': 'POST', 'url': '/login', 'status': '403', 'size': '512'} {'ip': '192.168.1.3', 'timestamp': '10/Mar/2024:14:25:15 +0000', 'method': 'GET', 'url': '/dashboard', 'status': '500', 'size': '2048'}


### **Analysis Output:**
Top 10 Requested URLs: /index.html 150 /login 120 /dashboard 100

HTTP Status Code Distribution: 200 800 404 50 500 30

Top 10 IPs Causing Errors: 192.168.1.2 20 192.168.1.3 15


### **Traffic Graph:**
📊 A **line graph** displaying hourly request trends.  
_(This will be generated using Matplotlib when running the script.)

