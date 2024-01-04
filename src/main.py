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
import utilities, measure_distance, turns, claw_function
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
claw_function.claw_motor = Motor(Ports.PORT10, False)
claw_function.claw_motor.set_max_torque(50, PERCENT)
brain.screen.print("claw_function.claw motor good!")
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




def _2a3a():
    smartdrive.drive(FORWARD)
    utilities.black_line()
    smartdrive.drive_for(FORWARD, 400, MM)
    leftmotor.spin_for(REVERSE, 440, DEGREES)
    wait(1)
    utilities.place_in_box()
    smartdrive.drive_for(REVERSE, 200, MM)
    claw_function.claw_down()
    smartdrive.drive_for(FORWARD, 200, MM)
    turns.right_turn()
    
utilities.place_holder_text()         
#Add color to Touchled:
touchled.set_color(Color.BLUE)

#Main code:
smartdrive.set_turn_velocity(5, PERCENT)
claw_function.claw_up()
turns.left_turn()
smartdrive.drive(FORWARD)
measure_distance.measure_distance_start()
turns.right_turn()
smartdrive.set_drive_velocity(60,PERCENT)
smartdrive.drive(FORWARD)
utilities.black_line()
smartdrive.set_drive_velocity(30, PERCENT)
measure_distance.measure_distance_c()
turns.right_turn()
smartdrive.set_turn_velocity(20, PERCENT)
smartdrive.drive(FORWARD)
measure_distance.measure_distance()
wait(1)
smartdrive.drive_for(REVERSE, 110, MM)
leftmotor.spin_for(REVERSE, 440, DEGREES)
wait(1, SECONDS)
claw_function.claw_up()
utilities.place_in_box()
turns.long_right_turn()
smartdrive.drive_for(FORWARD, 9, INCHES)
turns.right_turn()
_2a3a()

utilities.end_code()