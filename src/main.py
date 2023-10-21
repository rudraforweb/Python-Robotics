# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       rkumar                                                       #
# 	Created:      10/14/2023, 11:40:29 AM                                       #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Start of 'system check'.
brain=Brain()
touchled = Touchled(Ports.PORT9)
touchled.set_color(Color.RED)
brain.screen.set_font(FontType.MONO12)
brain.screen.print("Running system check:")
brain.screen.next_row()
wait(0.2, SECONDS)
brain.screen.print("Brain good!")
brain.screen.next_row()
wait(0.2, SECONDS)
brain_inertial = Inertial()
brain_inertial.calibrate()
brain.screen.print("Inertial good!")
wait(0.2, SECONDS)
brain.screen.next_row()
leftmotor=Motor(Ports.PORT7, False)
rightmotor=Motor(Ports.PORT12, True)
drivetrain=DriveTrain(leftmotor, rightmotor)
brain.screen.print("Drivetrain good!")
wait(0.2, SECONDS)
brain.screen.next_row()
claw_motor = Motor(Ports.PORT10, True)
claw_motor.set_max_torque(50, PERCENT)
brain.screen.print("Claw motor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
brain.screen.print("Touchled good!")
wait(0.2, SECONDS)
brain.screen.next_row()
color = ColorSensor(Ports.PORT11)
color.set_light(100, PERCENT)
brain.screen.print("Color sensor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
distance = Distance(Ports.PORT8)
brain.screen.print("Distance sensor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
brain.battery.capacity()
brain.screen.print("Battery good!")
wait(0.2, SECONDS)
touchled.set_color(Color.GREEN)
wait(1, SECONDS)
brain.screen.clear_screen()
brain.screen.set_cursor(2, 2)
brain.screen.set_font(FontType.PROP30)
brain.screen.print("Python-Robotics")
#End of "system check".

#Define functions:
def left_turn():
    drivetrain.turn_for(LEFT, 90, DEGREES)

def right_turn():
    drivetrain.turn_for(RIGHT, 90, DEGREES)

def end_code():
    touchled.set_color(Color.RED)
    drivetrain.stop()

def place_holder_text():
    brain.screen.clear_screen()
    brain.screen.set_cursor(2, 2)
    brain.screen.print("Python-Robotics")
    
def off_edge():
    if True:
        if distance.object_distance(INCHES) > 1:
            brain.screen.clear_screen()
            brain.screen.set_cursor(2, 2)
            brain.screen.print("Turning...")
            drivetrain.drive_for(REVERSE, 200, MM, wait=True)
            right_turn()
        else:
            drivetrain.drive(FORWARD)
            place_holder_text()   

#Add color to Touchled:
touchled.set_color(Color.BLUE)

#Claw Motor ready position:
claw_motor.spin_to_position(-40, DEGREES)

#Main code:

