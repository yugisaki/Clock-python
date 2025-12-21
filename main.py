import machine
from utime import sleep

led = machine.Pin("LED", machine.Pin.OUT)
led.on()
sleep(.25)
led.off()

import network

ssid = "You wifi name"
password = "your wifi password"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)

sleep(.2)
while not wlan.isconnected():
    sleep(.3)

import ntptime, time
ntptime.host = "pool.ntp.org"
ntptime.settime()
sleep(2)

while (True):
    try:
        current_time = time.localtime()
        year, month, day, hour, minute, sec, milsec, nanosec = current_time
        print(f"h: {hour + 1} min: {minute} sec: {sec}")
        sleep(1)

    except KeyboardInterrupt:
        print("bye")
        break