#!/usr/bin/env python
# -*- coding: utf-8 -*-

from machine import Pin
import utime

ECHO_PIN1 = 0
TRIG_PIN = 1
ECHO_PIN2 = 2
TRIG_PIN2 = 3

TRIG = Pin(TRIG_PIN, Pin.OUT)
TRIG2 = Pin(TRIG_PIN2, Pin.OUT)
ECHO1 = Pin(ECHO_PIN1, Pin.IN)
ECHO2 = Pin(ECHO_PIN2, Pin.IN)
#utime.sleep(0.3)

TRIG.value(1)
utime.sleep(0.00001)
TRIG.value(0)

while ECHO1.value() == 0:
    signaloff1 = utime.ticks_us()

while ECHO1.value() == 1:
    signalon1 = utime.ticks_us()

timepass1 = signalon1 - signaloff1
distance1 = timepass1 * 17
print("a"+str(distance1))

utime.sleep_ms(250)

TRIG2.value(1)
utime.sleep(0.00001)
TRIG2.value(0)

while ECHO2.value() == 0:
    signaloff2 = utime.ticks_us()

while ECHO2.value() == 1:
    signalon2 = utime.ticks_us()

timepass2 = signalon2 - signaloff2
distance2 = timepass2 * 17
print("b"+str(distance2))
