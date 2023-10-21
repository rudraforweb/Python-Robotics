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

# Brain should be defined by default
brain=Brain()
brain.screen.print("Program started!")
brain.screen.next_row()
brain.screen.print("Define: Brain defined")
brain.screen.next_row()
brain_inertial = Inertial()
brain.screen.print("Define: Inertial defined")
brain.screen.next_row()
leftmotor=Motor(Ports.PORT7, True)
brain.screen.print("Define: Left motor defined")
brain.screen.next_row()
rightmotor=Motor(Ports.PORT12, True)
brain.screen.print("Define: Right motor defined")
brain.screen.next_row()
claw_motor = Motor(Ports.PORT10, True)
brain.screen.print("Define: Claw motor defined")
wait(5)
brain.screen.clear_screen()



