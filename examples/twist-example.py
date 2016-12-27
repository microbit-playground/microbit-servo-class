# Rotates the servo depending on the microbit's rotation through the x axis.
# pressing button_a sweeps the servo from 0 degrees to 180 degrees
# pressing button_b gives 0 degrees then 180 degrees.
# Tested with SG90 servo @ 3.3v

from microbit import *

class Servo:

    """
    A simple class for controlling hobby servos.

    Args:
        pin (pin0 .. pin3): The pin where servo is connected.
        freq (int): The frequency of the signal, in hertz.
        min_us (int): The minimum signal length supported by the servo.
        max_us (int): The maximum signal length supported by the servo.
        angle (int): The angle between minimum and maximum positions.

    Usage:
        SG90 @ 3.3v servo connected to pin0
        = Servo(pin0).write_angle(90)
    """

    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        self.pin.write_digital(0)  # turn the pin off

    def write_angle(self, degrees=None):
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)



while True:
    if button_a.is_pressed():
        for x in range(0, 180, 5):
            # from 0 to 180 in steps of 5
            # write the angle of the step (x)
            Servo(pin0).write_angle(x)
            sleep(200)
    if button_b.is_pressed():
        # show maximum and minimum rotation if button
        # b pressed
        Servo(pin0).write_angle(0)
        sleep(2000)
        Servo(pin0).write_angle(180)
        sleep(2000)
    else:
        # rescale accelerometer x axis to between 0 and 180
        rescaled_angle = rescale((-1024, 1024), (0, 180), accelerometer.get_x())
        Servo(pin0).write_angle(rescaled_angle) # write rescaled angle
        sleep(200)