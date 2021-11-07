from owlet_monitor.helpers import safe_get


class OwletStatus:

    def __init__(self, properties: dict):
        self.device_sn = properties['DSN']
        self.input_properties = properties
        self.charge_status = safe_get(properties, [['CHARGE_STATUS', 'value']], 0)
        self.base_station_on = safe_get(properties, [['BASE_STATION_ON', 'value']], 0)
        self.heart_rate = "%d" % safe_get(properties, [['HEART_RATE', 'value'], ['REAL_TIME_VITALS', 'value', 'hr']], 0)
        self.oxygen_level = "%d" % safe_get(properties, [['OXYGEN_LEVEL', 'value'], ['REAL_TIME_VITALS', 'value', 'ox']], 0)
        self.movement_status = "wiggling" if safe_get(properties, [['MOVEMENT', 'value']], False) else "still"
        self.movement_level = "%d" % safe_get(properties, [['REAL_TIME_VITALS', 'value', 'mv']], 0)
        self.sock_off = "%d" % safe_get(properties, [['SOCK_OFF', 'value']], 0)
