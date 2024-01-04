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
smartdrive=SmartDrive(leftmotor, rightmotor,brain_inertial)
smartdrive.set_turn_velocity(20, PERCENT)
brain.screen.print("Drivetrain good!")
wait(0.2, SECONDS)
brain.screen.next_row()
claw_motor = Motor(Ports.PORT10, False)
claw_motor.set_max_torque(50, PERCENT)
brain.screen.print("Claw motor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
brain.screen.print("Touchled good!")
wait(0.2, SECONDS)
brain.screen.next_row()
color =ColorSensor(Ports.PORT11)
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
#End of "system check".

#Define functions:
claw_up_degrees = 40
claw_down_degrees = 5

right_turn_degrees = 90
left_turn_degrees = -90

def claw_up():
    claw_motor.spin_to_position(claw_up_degrees, DEGREES)
def claw_down():
    claw_motor.spin_to_position(claw_down_degrees, DEGREES)

def left_turn():
    smartdrive.set_turn_velocity(10, PERCENT)
    brain_inertial.set_heading(0, DEGREES)
    smartdrive.turn_to_rotation(left_turn_degrees, DEGREES)
    smartdrive.stop()
    wait(1)
def right_turn():
    smartdrive.set_turn_velocity(10, PERCENT)
    brain_inertial.set_heading(0, DEGREES)
    smartdrive.turn_to_rotation(right_turn_degrees, DEGREES)
    smartdrive.stop()
    wait(1)
def long_right_turn():
    leftmotor.spin_for(FORWARD, 430, DEGREES)
    leftmotor.stop()
def long_left_turn():
    rightmotor.spin_for(FORWARD, 430, DEGREES)
    rightmotor.stop()


def measure_distance_start():
    while distance.object_distance(INCHES) < 1:
        wait(0.1, SECONDS)
        smartdrive.set_drive_velocity(40, PERCENT)
        if distance.object_distance(INCHES) > 1:
            smartdrive.drive_for(FORWARD, 65, MM)
            smartdrive.stop()
            break
def measure_distance():
    while distance.object_distance(INCHES) < 1:
        wait(0.1, SECONDS)
        smartdrive.set_drive_velocity(40, PERCENT)
        if distance.object_distance(INCHES) > 1:
            smartdrive.stop()
            smartdrive.drive_for(REVERSE, 100, MM)
            break
def measure_distance_c():
    while distance.object_distance(INCHES) < 1:
        wait(0.1, SECONDS)
        smartdrive.set_drive_velocity(40)
        smartdrive.set_stopping(HOLD)
        if distance.object_distance(INCHES) > 1:
            smartdrive.stop()
            smartdrive.drive_for(REVERSE, 50, MM)
            break
def end_code():
    touchled.set_color(Color.RED)
    claw_down()
    smartdrive.stop()
    
def place_holder_text():
    brain.screen.clear_screen()
    brain.screen.set_font(FontType.PROP30)
    brain.screen.set_cursor(2, 2)
    brain.screen.print("  Python-Robotics")    

def black_line():
    while int(color.brightness()) >= 50: #type: ignore
        wait(0.1, SECONDS)
        smartdrive.set_stopping(HOLD)
        if int(color.brightness()) <= 50: #type: ignore 
            wait(0.1, SECONDS)
            claw_down()
            smartdrive.stop()
            wait(1, SECONDS)
            smartdrive.drive(FORWARD)
            break
def place_in_box():
    smartdrive.drive_for(REVERSE, 130, MM)
    claw_down()
    smartdrive.drive_for(FORWARD, 125, MM)
    claw_up()



def _2a3a():
    smartdrive.drive(FORWARD)
    black_line()
    smartdrive.drive_for(FORWARD, 400, MM)
    leftmotor.spin_for(REVERSE, 440, DEGREES)
    wait(1)
    place_in_box()
    smartdrive.drive_for(REVERSE, 200, MM)
    claw_down()
    smartdrive.drive_for(FORWARD, 200, MM)
    right_turn()
    
place_holder_text()         
#Add color to Touchled:
touchled.set_color(Color.BLUE)

#Main code:
smartdrive.set_turn_velocity(5, PERCENT)
claw_up()
left_turn()
smartdrive.drive(FORWARD)
measure_distance_start()
right_turn()
smartdrive.set_drive_velocity(60,PERCENT)
smartdrive.drive(FORWARD)
black_line()
smartdrive.set_drive_velocity(30, PERCENT)
measure_distance_c()
right_turn()
smartdrive.set_turn_velocity(20, PERCENT)
smartdrive.drive(FORWARD)
measure_distance()
wait(1)
smartdrive.drive_for(REVERSE, 110, MM)
leftmotor.spin_for(REVERSE, 440, DEGREES)
wait(1, SECONDS)
claw_up()
place_in_box()
long_right_turn()
smartdrive.drive_for(FORWARD, 9, INCHES)
right_turn()
_2a3a()

end_code()