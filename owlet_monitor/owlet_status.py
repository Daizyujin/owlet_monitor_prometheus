from owlet_monitor.helpers import safe_get


class OwletStatus:

    def __init__(self, properties: dict):
        self.device_sn = properties['DSN']
        self.charge_status = safe_get(properties, ['CHARGE_STATUS', 'value'], 0)
        self.base_station_on = safe_get(properties, ['BASE_STATION_ON', 'value'], 0)
        self.heart = "%d" % safe_get(properties, ['HEART_RATE', 'value'], 0)
        self.oxy = "%d" % safe_get(properties, ['OXYGEN_LEVEL', 'value'], 0)
        self.mov = "wiggling" if safe_get(properties, ['MOVEMENT', 'value'], False) else "still"
