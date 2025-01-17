#Backup Database
import requests
import os
import datetime


# Odoo server URL and database details
odoo_url = 'http://localhost' #Sesuaikan dengan nama domain odoo
db_name = 'db_name' #sesuaikan dengan nama database
admin_password = 'db_pass' #sesuaikan dengan password admin

now = datetime.datetime.now()

# Format tanggal dan waktu sesuai kebutuhan
date_str = now.strftime("%Y-%m-%d_%H-%M-%S")

# Backup file path
backup_path = f'/sesuaikan-dengan-lokasi-backup/{date_str}_{db_name}_backup.zip'

# Endpoint for database backup
backup_endpoint = f'{odoo_url}/web/database/backup'

# Parameters for the backup request
params = {
    'master_pwd': admin_password,
    'name': db_name,
    'backup_format': 'zip'
}

# Send the request to backup the database
response = requests.post(backup_endpoint, data=params, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Write the response content to a file
    with open(backup_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    print(f'Database backup successful: {backup_path}')
else:
    print(f'Failed to backup the database. Status code: {response.status_code}')
    print(response.text)