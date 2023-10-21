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
brain.screen.print("Define: Brain defined")
brain_inertial = Inertial()
brain.screen.print("Define: Inertial defined")
leftmotor=Motor(Ports.PORT7, True)
brain.screen.print("Define: Left motor defined")
rightmotor=Motor(Ports.PORT12, True)
brain.screen.print("Define: Right motor defined")
claw_motor = Motor(Ports.PORT10, True)
brain.screen.print("Define: Claw motor defined")



