import os
import subprocess
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='backup.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Configuration
SOURCE_DIR = '/path/to/source_directory'
REMOTE_USER = 'username'
REMOTE_SERVER = 'server_address'
REMOTE_DIR = '/path/to/remote_directory'
RSYNC_OPTIONS = '-avz'

def perform_backup():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_command = f'rsync {RSYNC_OPTIONS} {SOURCE_DIR} {REMOTE_USER}@{REMOTE_SERVER}:{REMOTE_DIR}/backup_{timestamp}'

    try:
        logging.info('Starting backup...')
        subprocess.check_output(backup_command, shell=True)
        logging.info('Backup completed successfully.')
    except subprocess.CalledProcessError as e:
        logging.error(f'Backup failed: {e.output.decode()}')

if __name__ == "__main__":
    perform_backup()
