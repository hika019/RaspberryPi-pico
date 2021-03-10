#!/usr/bin/env python
# -*- coding: utf-8 -*-

from machine import Pin
import utime

ECHO_PIN1 = 0
TRIG_PIN = 1
ECHO_PIN2 = 2
TRIG_PIN2 = 3

TRIG1 = Pin(TRIG_PIN, Pin.OUT)
TRIG2 = Pin(TRIG_PIN2, Pin.OUT)
ECHO1 = Pin(ECHO_PIN1, Pin.IN)
ECHO2 = Pin(ECHO_PIN2, Pin.IN)
#utime.sleep(0.3)



def get_distance(TRIG, ECHO):
    
    starttime = utime.ticks_us()
    #print(str(starttime))
    
    TRIG.value(1)
    utime.sleep(0.00001)
    TRIG.value(0)
    
    while ECHO.value() == 0:
        signaloff = utime.ticks_us()
        if(signaloff > (starttime + 100000)):
            return 5000
    
    while ECHO.value() == 1:
        signalon = utime.ticks_us()
    
    timepass = signalon - signaloff
    distance = timepass * 17
    #print(str(signaloff))
    
    return distance/1000#cm


print("a"+str(get_distance(TRIG1, ECHO1)))


print("b"+str(get_distance(TRIG2, ECHO2)))

