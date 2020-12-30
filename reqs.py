"""Utilities to work with an API of flespi platform"""


from datetime import datetime
import requests
import pytz



def get_telemetry(flespi_token, device_number):
    """Python wrapper on flesp API to get the latest telemetry json.

    Parameters:
    -----------
    flespi_token: str
        Flespi token generated on the flespi platform.
    device_number : int
        Device number integrated with a flespi platform. Device is a GPS tracker.

    Returns:
    --------
    telemetry: dict
        The latest telemetry from the device.
    """
    headers = {
        'Accept': 'application/json',
        'Authorization': 'FlespiToken {}'.format(flespi_token)}
    response = requests.get('https://flespi.io/gw/devices/{}/telemetry'.format(device_number),
                             headers=headers)
    telemetry = response.json()['result'][0]['telemetry']

    return telemetry

def convert_unix_ts(timestamp, timezone = "Europe/Berlin"):
    """Utility function to help converting flespi utc unix time output to human readable.

    Parameters:
    -----------
    timestamp: int
        Unix time generated py flespi platform.

    timezone: str
        Time zone of the user. Defaoults to: Europe/Berlin

    Returns:
    --------
    date: str
        Human readable time with a following format: %Y-%m-%d %H:%M:%S
    """
    timezone = pytz.timezone(timezone)
    date = datetime.fromtimestamp(timestamp, timezone)

    return date.strftime('%Y-%m-%d %H:%M:%S')
