# Prometheus metrics

Prometheus metrics are hosted on `localhost:9090/`

## Example metrics

```prometheus
# HELP owlet_base_status_on Base Station Power
# TYPE owlet_base_status_on gauge
owlet_base_status_on{dsn="ASDFASDFASDF1234"} 0.0
# HELP owlet_heart_rate Heart rate
# TYPE owlet_heart_rate gauge
owlet_heart_rate{dsn="ASDFASDFASDF1234"} 103.0
# HELP owlet_oxygen_level Oxygen Status
# TYPE owlet_oxygen_level gauge
owlet_oxygen_level{dsn="ASDFASDFASDF1234"} 96.0
# HELP owlet_wiggle_level Wiggle level (movement)
# TYPE owlet_wiggle_level gauge
owlet_wiggle_level{dsn="ASDFASDFASDF1234"} 0.0
# HELP owlet_api_updates_total Number of Owlet API updates
# TYPE owlet_api_updates_total counter
owlet_api_updates_total{dsn="ASDFASDFASDF1234"} 1.0
# HELP owlet_api_updates_created Number of Owlet API updates
# TYPE owlet_api_updates_created gauge
owlet_api_updates_created{dsn="ASDFASDFASDF1234"} 1.636335496524408e+09
# HELP owlet_battery_level Battery level (percentage)
# TYPE owlet_battery_level gauge
owlet_battery_level{dsn="ASDFASDFASDF1234"} 60.0
# HELP owlet_charge_status Charging status
# TYPE owlet_charge_status gauge
owlet_charge_status{dsn="ASDFASDFASDF1234"} 0.0
```