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
colorsensor = ColorSensor(Ports.PORT11)
brain.screen.print("Color sensor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
brain.screen.print("All good!")
wait(0.5, SECONDS)
brain.screen.clear_screen()
brain.screen.set_cursor(2, 2)
brain.screen.set_font(FontType.PROP30)
brain.screen.print(" Python-Robotics")
#End of "system check".

#Add color to Touchled:
touchled.set_color(Color.BLUE)
#Claw Motor ready position:
claw_motor.spin_to_position(-40, DEGREES)






