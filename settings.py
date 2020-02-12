from pytz import timezone

# InfluxDB configuration
INFLUXDB_HOST = '127.0.0.1'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = None
INFLUXDB_PASSWORD = None
INFLUXDB_DATABASE = 'database'
INFLUXDB_TIMEOUT = 10

# Timezone Settings
TIMEZONE = timezone("CET")

try:
    from local_settings import *
except ImportError:
    pass
