import settings
from influxdb import InfluxDBClient

class InfluxDB:
    """
    Class for the InfluxDB client
    """

    def __init__(self):
        self.client = InfluxDBClient(
            settings.INFLUXDB_HOST,
            settings.INFLUXDB_PORT,
            settings.INFLUXDB_USERNAME,
            settings.INFLUXDB_PASSWORD,
            settings.INFLUXDB_DATABASE,
            timeout=getattr(settings, 'INFLUXDB_TIMEOUT', 10),
            ssl=getattr(settings, 'INFLUXDB_SSL', False),
            verify_ssl=getattr(settings, 'INFLUXDB_VERIFY_SSL', False),
        )

    def write(self, json):
        self.client.write_points(json)

    def query(self, query):
        result = self.client.query(query)

        return result.raw