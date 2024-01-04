from vex import *
from claw_function import *

brain=Brain()
brain_inertial = Inertial()
touchled = Touchled(Ports.PORT9)
leftmotor=Motor(Ports.PORT7, False)
rightmotor=Motor(Ports.PORT12, True)
smartdrive=SmartDrive(leftmotor, rightmotor,brain_inertial)

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