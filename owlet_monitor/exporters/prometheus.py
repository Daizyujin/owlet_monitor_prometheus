from ..owlet_status import OwletStatus
from .base_exporter import BaseExporter
from prometheus_client import Gauge, start_http_server, Counter


class PrometheusExporter(BaseExporter):

    def __init__(self):
        """Starts Prometheus web server and creates metrics"""
        start_http_server(8000)
        self.metric_base_station_on = Gauge('owlet_base_status_on', 'Base Station Power', ['dsn'])
        self.metric_heart = Gauge('owlet_heart_rate', 'Heart rate', ['dsn'])
        self.metric_oxy = Gauge('owlet_oxygen_level', 'Oxygen Status', ['dsn'])
        self.metric_wiggle_level = Gauge('owlet_wiggle_level', 'Wiggle level (movement)', ['dsn'])
        self.metric_owlet_api_updates = Counter('owlet_api_updates', 'Number of Owlet API updates', ['dsn'])
        self.metric_battery_level = Gauge('owlet_battery_level', 'Battery level (percentage)', ['dsn'])
        self.metric_charge_status = Gauge('owlet_charge_status', 'Charging status', ['dsn'])

    def export(self, status: OwletStatus):
        """Maps OwletStatus to Prometheus metrics and updates them"""
        self.metric_base_station_on.labels(status.device_sn).set(status.base_station_on)
        self.metric_heart.labels(status.device_sn).set(status.heart_rate)
        self.metric_oxy.labels(status.device_sn).set(status.oxygen_level)
        self.metric_battery_level.labels(status.device_sn).set(status.battery_level)
        self.metric_charge_status.labels(status.device_sn).set(status.charge_status)
        self.metric_owlet_api_updates.labels(status.device_sn).inc()
        self.metric_wiggle_level.labels(status.device_sn).set(status.movement_level)

