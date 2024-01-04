from vex import *

leftmotor=Motor(Ports.PORT7, False)
rightmotor=Motor(Ports.PORT12, True)
brain_inertial = Inertial()
brain_inertial.calibrate()
smartdrive=SmartDrive(leftmotor, rightmotor,brain_inertial)

right_turn_degrees = 85
left_turn_degrees = -85

def left_turn():
    smartdrive.set_turn_velocity(10, PERCENT)
    brain_inertial.set_heading(0, DEGREES)
    smartdrive.turn_to_heading(left_turn_degrees, DEGREES)
    smartdrive.stop()
    wait(1)
def right_turn():
    smartdrive.set_turn_velocity(10, PERCENT)
    brain_inertial.set_heading(0, DEGREES)
    smartdrive.turn_to_heading(right_turn_degrees, DEGREES)
    smartdrive.stop()
    wait(1)
def long_right_turn():
    leftmotor.spin_for(FORWARD, 430, DEGREES)
    leftmotor.stop()
def long_left_turn():
    rightmotor.spin_for(FORWARD, 430, DEGREES)
    rightmotor.stop()
