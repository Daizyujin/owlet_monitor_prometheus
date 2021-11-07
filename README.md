This Python script monitors [Owlet Smart Sock](https://owletcare.com/)
statistics such as heart rate, oxygen level, etc. Its implementation was made
possible after reverse engineering the Owlet Android app version 1.1.41
(latest version as of April 2020) to understand how the data is recorded
and fetched.

`owlet_monitor` prints the statistics every 10 seconds on stdout in CSV format.
Your owlet username and password must be passed via environment variables. Log
messages are printed on stderr.

Usage:

```
$ env OWLET_USER=xxx@xxx.xxx OWLET_PASS=xxx ./owlet_monitor >logfile
Logging in
Auth token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Getting DSN
Found Owlet monitor device serial number ACxxxxxxxxxxxxx
AC000W00XXXXXXX Status: 1532665440, 131, 100, still
AC000W00XXXXXXX Status: 1532665450, 125, 100, still
[...]
```

(If you are using an Owlet in Europe, set the `OWLET_REGION` environment variable to `europe` to use the European servers otherwise you may get a `400`/`EMAIL_NOT_FOUND` error.)

Each CSV line consists of:
* timestamp (seconds since UNIX Epoch time)
* heart rate (BPM)
* blood oxygen level (%)
* movement (from sock sensor: baby still or wiggling)
* device serial number (useful for multiple babies/owlet devices)

## Technical details

* The owlet account email and password are validated using [Firebase Authentication](https://firebase.google.com/docs/auth) — this returns a JWT
* A GET request authenticated with the JWT is made to https://ayla-sso.owletdata.com/mini/ — this returns a `mini_token`
* The `mini_token` is used to sign into the [Ayla Networks cloud API](https://developer.aylanetworks.com/apibrowser/)
* Heart rate, oxygen level, etc are periodically fetched from the Ayla API

Many details (app id/secret, property names, apparent need to set APP\_ACTIVE=1)
were reverse-enginered from Owlet's Android app.

You can place "index.html" and "logfile" in a directory served by a web server
and browse "index.html?logfile" to see a chart.

### API response examples

```
REAL_TIME_VITALS
{'type': 'Property', 'base_type': 'string', 'read_only': True, 'direction': 'output', 'scope': 'user', 'data_updated_at': '2021-11-07T01:35:05Z', 'key': 0000, 'device_key': 0000, 'product_name': '0000', 'track_only_changes': False, 'display_name': 'Real-Time Vitals', 'host_sw_version': False, 'time_series': False, 'derived': False, 'app_type': None, 'recipe': None, 'value': '{"ox":99,"hr":134,"mv":0,"sc":2,"st":33,"bso":1,"bat":95,"btt":925,"chg":0,"aps":0,"alrt":0,"ota":0,"srf":0,"rsi":55,"sb":0}', 'denied_roles': [], 'ack_enabled': False, 'retention_days': 30, 'ack_status': None, 'ack_message': None, 'acked_at': None}
```
