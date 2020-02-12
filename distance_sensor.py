import RPi.GPIO as GPIO
import time

GPIO_TRIGGER = 13
GPIO_ECHO = 6


class HCSR04:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

    def get_distance(self):
        GPIO.output(GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime

        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        if distance > 400: distance = 400.0

        return distance

    def detect_garbage(self):
        total = 0
        errors = 0
        for i in range(5):
            current = self.get_distance()
            if current >= 400:
                errors += 1
                i -= 1
                if errors > 5: break
            else:
                total += current
            time.sleep(0.5)

        avg_distance = total / i + 1

        return avg_distance < 50
