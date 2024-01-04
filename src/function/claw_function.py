from vex import *

claw_motor = Motor(Ports.PORT10, False)

claw_up_degrees = 40
claw_down_degrees = 5

def claw_up():
    claw_motor.spin_to_position(claw_up_degrees, DEGREES)
def claw_down():
    claw_motor.spin_to_position(claw_down_degrees, DEGREES)
