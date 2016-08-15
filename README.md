# Class for Servo Control in Python on the Microbit

This is a simple class for controlling servos on the microbit in Python. Cut and paste the class to the top of the program.

### Example Usage

Paste the class on the line after `import * from microbit`.

##### 180 degree SG90 Hobby Servo @ 3.3v on pin0:

```
sv1 = Servo(pin0)
sv1.write_angle(50) # turn servo to 50 degrees 
````
##### 180 degree SG90 Hobby Servo @ 4.8v on pin0:

_note how the min_us changes with the voltage supply_

```
sv1 = Servo(pin0, min_us=1000, max_us=2000)
sv1.write_angle(180) # turn servo to 180 degrees 
````

##### 180 degree Parallax 900-00005 (BS1) Servo @ 6v on pin0:

```
sv1 = Servo(pin0, min_us=750, max_us=2250)
sv.write_angle(10)
```

[Code from The Sheep on Bitbucket](https://bitbucket.org/thesheep/micropython-servo/src/f562a6abeaf0e83b752838df7cd31d88ea10b2c7?at=default) and made compatable (and worse) by me. Rescale function by [Tom Viner](https://www.youtube.com/channel/UCmA_ydtrCCQ7twKpovboiPA)