logs_file = "server_logs.log"

with open(logs_file, "r") as file:
    for line in file:
        print(line.strip())

#Output will look like this 
# 192.168.1.1 - - [10/Mar/2024:14:23:45 +0000] "GET /index.html HTTP/1.1" 200 1024
# 192.168.1.2 - - [10/Mar/2024:14:24:05 +0000] "POST /login HTTP/1.1" 403 512
# 192.168.1.3 - - [10/Mar/2024:14:25:15 +0000] "GET /dashboard HTTP/1.1" 500 2048