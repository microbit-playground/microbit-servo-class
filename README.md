# Class for Servo Control in Python on the Microbit

This is a simple class for controlling servos on the microbit in Python. 

## Using the Modules

There are two ways:

#### Quick and Easy

Cut and paste [the class in servo.py](https://github.com/microbit-playground/microbit-servo-class/blob/master/servo.py) to the top of the program. 

See [here for an example](https://github.com/microbit-playground/microbit-servo-class/blob/master/examples/twist-example.py).

#### Proper Way

The correct approach is to copy the module to the filesystem. It can then be accessed in the same way the `microbit` module is imported at the start of each program.

The are two steps: copying the module to the microbit and importing the module into your program.


##### Copying the module:

1. Save [the module](https://github.com/microbit-playground/microbit-servo-class/blob/master/servo.py) to your computer.

2. Copy the downloaded module to the `/mu_code/` directory in the root of your home directory.

3. Flash your program to mu.

4. An error message will scroll across the screen about the lack of the servo module.

5. Once it has finished, click the 'files' icon in mu and upload the `servo.py` file to your microbit.

6. Press reset on your microbit. When the program runs again it will load the module.

##### In your program:

```
from microbit import *

# from servo.py import the Servo class
from servo import Servo

# this can now be accessed within your program
sv1 = Servo(pin0)
sv1.write_angle(50) # turn servo to 50 degrees 
```

## Code Examples

##### 180 degree SG90 Hobby Servo @ 3.3v on pin0:

```
sv1 = Servo(pin0)
sv1.write_angle(50) # turn servo to 50 degrees 
````
##### 180 degree SG90 Hobby Servo @ 4.8v on pin0:

_note how min_us and max_us changes. These details will be on the servo's datasheet._

```
sv1 = Servo(pin0, min_us=1000, max_us=2000)
sv1.write_angle(180) # turn servo to 180 degrees 
````

##### 180 degree Parallax 900-00005 (BS1) Servo @ 6v on pin1:

```
sv1 = Servo(pin1, min_us=750, max_us=2250)
sv.write_angle(10)
```

[Code from The Sheep on Bitbucket](https://bitbucket.org/thesheep/micropython-servo/src/f562a6abeaf0e83b752838df7cd31d88ea10b2c7?at=default) and made compatable (and worse) by me. Rescale function by [Tom Viner](https://www.youtube.com/channel/UCmA_ydtrCCQ7twKpovboiPA)