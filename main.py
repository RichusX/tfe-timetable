import requests
import json

base_url = "https://tfeapp.com/api/website/stop_times.php?stop_id="
stop_id = "6200241910"

url = base_url + stop_id
r = requests.get(url)

departures = {}


if r.ok:
    rdata = r.json()

    for service in rdata["services"]:
        bus_no = int(service["service_name"])
        if bus_no not in departures:
            departures[bus_no] = []

        for departure in service["departures"]:
            departures[bus_no].append(departure["minutes"])

    print(departures)
