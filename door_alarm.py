import Adafruit_BBIO.ADC as ADC
import time
import twitter
import settings
from subprocess import call

SENSOR_PIN = 'P9_40'
DOOR_CLOSED_DETECTION_PERIOD_SECS = 2 
SAMPLE_FREQUENCY = 0.1
SAMPLES_REQUIRED = DOOR_CLOSED_DETECTION_PERIOD_SECS * (1/SAMPLE_FREQUENCY)
SENSOR_THRESHOLD = 0.8

def post_to_twitter(msg):
    """Send a personal message to Twitter"""
    api = twitter.Api(consumer_key=settings.CONSUMER_KEY,
                      consumer_secret=settings.CONSUMER_SECRET,
                      access_token_key=settings.ACCESS_TOKEN_KEY,
                      access_token_secret=settings.ACCESS_TOKEN_SECRET)
    api.PostDirectMessage(text=msg,
                          screen_name=settings.TWITTER_SCREEN_NAME)

def monitor_sensor():
    """Read the sensor value and detect an alarm condition."""

    print "Starting to monitor sensor"
    post_to_twitter("Door Entry Alarm: started")
    ADC.setup()

    is_open = False
    samples_counter = 0
    while True:
        reading = ADC.read(SENSOR_PIN)
        if is_open == False:
            if reading > SENSOR_THRESHOLD:
                samples_counter += 1
                if samples_counter >= SAMPLES_REQUIRED:
                    is_open = True
                    print "Door opened"
                    post_to_twitter("Door opened")
                    samples_counter = 0
            else:
                samples_counter = 0
        elif is_open == True:
            if reading <= SENSOR_THRESHOLD:
                is_open = False
                print "Door closed"
                post_to_twitter("Door closed")
                samples_counter = 0
        time.sleep(SAMPLE_FREQUENCY)

monitor_sensor()
