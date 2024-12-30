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
import psycopg2
from config import get_mac_address, get_database, get_host, get_port, get_user, get_password

mac_address = get_mac_address()
poller = MiFloraPoller(mac_address, BluepyBackend)

temp = poller.parameter_value(MI_TEMPERATURE)
light = poller.parameter_value(MI_LIGHT)
moisture = poller.parameter_value(MI_MOISTURE)
conductivity = poller.parameter_value(MI_CONDUCTIVITY)
battery = poller.parameter_value(MI_BATTERY)


con = psycopg2.connect(database=get_database(),
                        host=get_host(),
                        user=get_user(),
                        password=get_password(),
                        port=get_port())

cursor = con.cursor()

cursor.execute("""
    INSERT INTO readings (mac_address, plant_name, temperature, light, moisture, conductivity, battery)VALUES
        (%s,%s,%s,%s,%s,%s,%s)""",(mac_address, "test", temp, light, moisture, conductivity, battery) )

con.commit()
con.close()
