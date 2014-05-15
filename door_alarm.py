import Adafruit_BBIO.ADC as ADC
import time
import twitter
import settings

SENSOR_PIN = 'P9_40'
DOOR_CLOSED_DETECTION_PERIOD_SECS = 2
SAMPLE_FREQUENCY = 0.1
DOOR_CLOSED_SAMPLES = DOOR_CLOSED_DETECTION_PERIOD_SECS * (1/SAMPLE_FREQUENCY)
SENSOR_THRESHOLD = 0.1

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

    post_to_twitter("Door Entry Alarm: started")
    ADC.setup()

    is_open = True
    closed_samples_counter = 0
    while True:
        reading = ADC.read(SENSOR_PIN)
        if is_open == False and reading > SENSOR_THRESHOLD:
            print "Door opened"
            post_to_twitter("Door opened")
            is_open = True
        elif is_open == True:
            if reading < SENSOR_THRESHOLD:
                closed_samples_counter += 1
                if closed_samples_counter >= DOOR_CLOSED_SAMPLES:
                    is_open = False
                    print "Door closed"
                    post_to_twitter("Door closed")
                    closed_samples_counter = 0
            else:
                closed_samples_counter = 0
        time.sleep(SAMPLE_FREQUENCY)

monitor_sensor()
