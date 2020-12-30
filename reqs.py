import yaml
import requests
from datetime import datetime
import pytz

with open("secrets_private.yaml", 'r') as f:
    secrets_loaded = yaml.safe_load(f)

credentials = secrets_loaded['credentials']
device_number = credentials['device_number']
flespi_token = credentials['flespi_token']

def get_telemetry(flespi_token, device_number):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'FlespiToken {}'.format(flespi_token)}
    response = requests.get('https://flespi.io/gw/devices/{}/telemetry'.format(device_number), headers=headers)
    telemetry = response.json()['result'][0]['telemetry']
    
    return telemetry

if __name__ == "__main__":
    print(get_telemetry(flespi_token=flespi_token, device_number=device_number))