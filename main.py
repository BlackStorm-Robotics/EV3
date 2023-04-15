#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, UltrasonicSensor)
from pybricks.tools import wait



#initialize the ev3 brick
ev3 = EV3Brick()
 
#initialize the motors at port A and D
motorR = Motor(Port.A)
motorL = Motor(Port.D)

#initialize a ultrasonic sensor at port 1
eyes = UltrasonicSensor(Port.S1)


#Function creation 
def motorRun(a, b):
    motorR.run(a)
    motorL.run(b)

search = False

while True:
    #check ultrassonic sensor distance
    a = eyes.distance()
    #sumo
    while search == False:
        a = eyes.distance()
        b = ev3brick.buttons()
        if Button.UP in b:
            if a <= 400:
                motorRun(1000, 1000)

            else:
                motorRun(400, -400)
    
        elif Button.CENTER in b:
            search = True
          
    #No colision
    while search == True:
        a = eyes.distance()
        b = ev3brick.buttons()
        if a <= 400:
            motorRun(400, -400)
    
        else:
            motorRun(1000, 1000)
        
        if Button.UP in b:
            motorRun(0, 0)
            search = False
