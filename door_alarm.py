import Adafruit_BBIO.ADC as ADC
import time

SENSOR_PIN = 'P9_40'
DOOR_CLOSED_DETECTION_PERIOD_SECS = 2
SAMPLE_FREQUENCY = 0.1
DOOR_CLOSED_SAMPLES = DOOR_CLOSED_DETECTION_PERIOD_SECS * (1/SAMPLE_FREQUENCY)
SENSOR_THRESHOLD = 0.1

def monitor_sensor():
    """Read the sensor value and detect an alarm condition."""
    ADC.setup()

    is_open = True
    closed_samples_counter = 0
    while True:
        reading = ADC.read(SENSOR_PIN)
        if is_open == False and reading > SENSOR_THRESHOLD:
            print "Door opened"
            is_open = True
        elif is_open == True:
            if reading < SENSOR_THRESHOLD:
                closed_samples_counter += 1
                if closed_samples_counter >= DOOR_CLOSED_SAMPLES:
                    is_open = False
                    print "Door closed"
                    closed_samples_counter = 0
            else:
                closed_samples_counter = 0
        time.sleep(SAMPLE_FREQUENCY)

monitor_sensor()
