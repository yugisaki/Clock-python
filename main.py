import machine
from utime import sleep

# Led for init
led = machine.Pin("LED", machine.Pin.OUT)
led.on()
sleep(.25)
led.off()

# Network
import network

ssid = "You wifi name"
password = "your wifi password"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)

sleep(.2)
while not wlan.isconnected():
    sleep(.3)

import ntptime, time # set time server
ntptime.host = "pool.ntp.org"
ntptime.settime()
sleep(2)

import Drivers

epd = Drivers.EPD_2in9()
tp = Drivers.ICNT86()
icnt_dev = Drivers.ICNT_Development()
icnt_old = Drivers.ICNT_Development()

epd.init()
tp.ICNT_Init()


epd.fill(0xff)
epd.display_Base(epd.buffer)
epd.text("clock-py",35,10,0x00)
epd.display_Partial(epd.buffer)

while (True):
    try: # main loop

        # get time
        current_time = time.localtime()
        year, month, day, hour, minute, sec, milsec, nanosec = current_time 

        #w rite buffer
        epd.text(f"h: {hour + 1}",15,75,0x00)
        epd.text(f"min: min:{minute}",15,75+12,0x00)
        epd.text(f"sec: {sec}",15,75+12+12,0x00)
        epd.display_Partial(epd.buffer)

        # reset buffer
        epd.text(f"h: {hour + 1}",15,75,0xff)
        epd.text(f"min: min:{minute}",15,75+12,0xff)
        epd.text(f"sec: {sec}",15,75+12+12,0xff)
        

    except KeyboardInterrupt:
        print("bye")
        break