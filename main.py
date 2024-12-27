#!/usr/bin/python3

from miflora.miflora_poller import (
    MI_BATTERY,
    MI_CONDUCTIVITY,
    MI_LIGHT,
    MI_MOISTURE,
    MI_TEMPERATURE,
    MiFloraPoller,
)
from btlewrap.bluepy import BluepyBackend
import sqlite3
from config import get_mac_address

mac_address = get_mac_address()
poller = MiFloraPoller(mac_address, BluepyBackend)

temp = poller.parameter_value(MI_TEMPERATURE)
light = poller.parameter_value(MI_LIGHT)
moisture = poller.parameter_value(MI_MOISTURE)
conductivity = poller.parameter_value(MI_CONDUCTIVITY)
battery = poller.parameter_value(MI_BATTERY)

con = sqlite3.connect('miflora')
cur = con.cursor()
cur.execute("""
    INSERT INTO readings (mac_address, plant_name, temperature, light, moisture, conductivity, battery)VALUES
        (?,?,?,?,?,?,?)""",(mac_address, "test", temp, light, moisture, conductivity, battery) )

con.commit()
con.close()