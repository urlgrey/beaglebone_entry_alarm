import Adafruit_BBIO.ADC as ADC
import time

sensor_pin = 'P9_40'
is_open=True
close_counter=0

ADC.setup()

while True:
    reading = ADC.read(sensor_pin)
    if is_open == False and reading > 0.1:
        print "Door opened"
        is_open=True
    elif is_open == True:
        if reading < 0.1:
            close_counter += 1
            if close_counter >= 30:  # door sensor must read low for 3 seconds
                is_open=False
                print "Door closed"
                close_counter = 0
        else:
            close_counter=0          # reset the close counter, false alarm
    time.sleep(0.1)

