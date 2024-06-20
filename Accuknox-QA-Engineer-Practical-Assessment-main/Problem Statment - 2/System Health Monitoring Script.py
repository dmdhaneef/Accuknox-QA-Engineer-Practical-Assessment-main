import psutil
import logging
import time

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {usage}%')
    return usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    usage = memory.percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {usage}%')
    return usage

def check_disk_usage():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        logging.warning(f'Low disk space detected: {usage}% used')
    return usage

def log_running_processes():
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]
    logging.info(f'Running processes: {processes}')

def monitor_system():
    while True:
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_usage()
        log_running_processes()
        
        logging.info(f'CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%, Disk Usage: {disk_usage}%')
        
        # Wait for 60 seconds before the next check
        time.sleep(60)

if __name__ == "__main__":
    monitor_system()
