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
brain_inertial = Inertial()
motorone=Motor(Ports.PORT7, True)
motortwo=Motor(Ports.PORT12, True)
claw_motor = Motor(Ports.PORT4, True)



