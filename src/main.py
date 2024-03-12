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
touchledleft = Touchled(Ports.PORT9)
touchledright = Touchled(Ports.PORT6)
touchledright.set_color(Color.RED)
touchledleft.set_color(Color.RED)
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
pusher = Motor(Ports.PORT5, True)
pusher.set_max_torque(100, PERCENT)
brain.screen.print("Claw motor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
brain.screen.print("Touchleds good!")
wait(0.2, SECONDS)
brain.screen.next_row()
color =ColorSensor(Ports.PORT11)
color.set_light(100, PERCENT)
brain.screen.print("Color sensor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
distance = Distance(Ports.PORT1)
brain.screen.print("Distance sensor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
brain.battery.capacity()
brain.screen.print("Battery good!")                 
wait(1, SECONDS)
brain.screen.clear_screen()
#End of "system check".

#Define functions:
claw_up_degrees = 40
claw_down_degrees = 5

#Touchleds:
def default_lights():
    touchledright.set_brightness(5)
    touchledright.set_color(Color.RED)
    touchledleft.set_brightness(5)
    touchledleft.set_color(Color.RED)
def stop():
    touchledright.set_brightness(100)
    touchledright.set_color(Color.RED)
    touchledleft.set_brightness(100)
    touchledleft.set_color(Color.RED)
    smartdrive.stop()
    wait(100, MSEC)
    default_lights()
def reverse_lights():
    touchledright.set_brightness(100)
    touchledright.set_color(Color.WHITE)
    touchledleft.set_brightness(100)
    touchledleft.set_color(Color.WHITE)
def blink_orange_left():
    touchledleft.set_brightness(100)
    touchledleft.set_color(Color.ORANGE)
    wait(400)  # Wait for 500 milliseconds (0.5 seconds)
    touchledleft.set_brightness(0)
    wait(400)  # Wait for another 500 milliseconds (0.5 seconds)
    touchledleft.set_brightness(100)
def blink_orange_right():
    touchledright.set_brightness(100)
    touchledright.set_color(Color.YELLOW_ORANGE)
    wait(400)  # Wait for 500 milliseconds (0.5 seconds)
    touchledright.set_brightness(0)
    wait(400)  # Wait for another 500 milliseconds (0.5 seconds)
    touchledright.set_brightness(100)

#Claw motor:
def claw_up():
    claw_motor.spin_to_position(claw_up_degrees, DEGREES)
def claw_down():
    claw_motor.spin_to_position(claw_down_degrees, DEGREES)

#Turns:
def left_turn(left_turn_degrees):
    blink_orange_left()
    smartdrive.turn_for(LEFT, left_turn_degrees, DEGREES)
    smartdrive.turn_for(LEFT, 0, DEGREES)
    default_lights()
def right_turn(right_turn_degrees):
    blink_orange_right()
    smartdrive.turn_for(RIGHT, right_turn_degrees, DEGREES)
    smartdrive.turn_for(RIGHT, 0, DEGREES)
    default_lights()
def long_right_turn():
    touchledleft.set_brightness(100)
    touchledleft.set_color(Color.WHITE)
    blink_orange_right()
    rightmotor.spin_for(REVERSE, 470, DEGREES)
    rightmotor.stop()
    touchledleft.set_brightness(0)
    touchledright.set_brightness(0)
def long_left_turn():
    touchledright.set_brightness(100)
    touchledright.set_color(Color.WHITE)
    blink_orange_left()
    leftmotor.spin_for(REVERSE, 450, DEGREES)
    leftmotor.stop()
    touchledleft.set_brightness(0)
    touchledright.set_brightness(0)

#Measure distances:
def measure_distance_start():
    while distance.object_distance(INCHES) < 2:
        wait(0.1, SECONDS)
        smartdrive.set_drive_velocity(40, PERCENT)
        if distance.object_distance(INCHES) > 2:
            smartdrive.drive_for(FORWARD, 65, MM)
            stop()
            break
def measure_distance():
    while distance.object_distance(INCHES) < 2:
        wait(0.1, SECONDS)
        if distance.object_distance(INCHES) > 2:
            stop()
            wait(1)
            reverse_lights()
            smartdrive.drive_for(REVERSE, 100, MM)
            default_lights()
            break
def measure_distance_c():
    while distance.object_distance(INCHES) < 2:
        wait(0.1, SECONDS)
        smartdrive.set_drive_velocity(40)
        smartdrive.set_stopping(HOLD)
        if distance.object_distance(INCHES) > 2:
            stop()
            reverse_lights()
            smartdrive.drive_for(REVERSE, 50, MM)
            default_lights()
            break 
def right_measure_distance():
    smartdrive.drive(FORWARD)
    while distance.object_distance(INCHES) < 2:
            wait(0.1, SECONDS)
            smartdrive.set_drive_velocity(40, PERCENT)
            if distance.object_distance(INCHES) > 2:
                stop()
                smartdrive.drive_for(REVERSE, 50, MM)
                leftmotor.spin_for(FORWARD, 440, DEGREES)
                stop()
                break
def left_measure_distance():
    smartdrive.drive(FORWARD)
    while distance.object_distance(INCHES) < 2:
            wait(0.1, SECONDS)
            smartdrive.set_drive_velocity(40, PERCENT)
            if distance.object_distance(INCHES) > 2:
                stop()
                smartdrive.drive_for(REVERSE, 50, MM)
                rightmotor.spin_for(FORWARD, 440, DEGREES)
                stop()
                break

#Others:
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
            stop()
            wait(1, SECONDS)
            smartdrive.drive(FORWARD)
            break
def place_in_box():
    claw_up()
    pusher.spin_to_position(70, DEGREES)
    pusher.spin_to_position(2, DEGREES)
    claw_down()

#Main code functions:
def start():
    if int(color.brightness()) <= 50: #type: ignore 
        wait(0.1, SECONDS)
        stop()
        brain.screen.set_cursor(1,1)
        brain.screen.print("Bit 1: Black")
        smartdrive.drive(FORWARD)
    else:
        brain.screen.set_cursor(1,1)
        brain.screen.print("Bit 1: White")


    smartdrive.drive_for(FORWARD, 40, MM)


    if int(color.brightness()) <= 50: #type: ignore 
            wait(0.1, SECONDS)
            stop()
            brain.screen.set_cursor(2,1)
            brain.screen.print("Bit 2: Black")
            smartdrive.drive(FORWARD)
    else:
        brain.screen.set_cursor(2,1)
        brain.screen.print("Bit 2: White")

    smartdrive.drive_for(FORWARD, 40, MM)

    if int(color.brightness()) <= 50: #type: ignore 
            wait(0.1, SECONDS)
            stop()
            brain.screen.set_cursor(3,1)
            brain.screen.print("Bit 3: Black")
            stop()

    else:
        brain.screen.set_cursor(3,1)
        brain.screen.print("Bit 3: White")
        stop()
         
def _1c():   
    smartdrive.drive(FORWARD)
    right_measure_distance()
    smartdrive.set_drive_velocity(60,PERCENT)
    smartdrive.drive(FORWARD)
    black_line()
    smartdrive.set_drive_velocity(30, PERCENT)
    measure_distance_c()
    right_turn(87)
    smartdrive.set_turn_velocity(20, PERCENT)
    smartdrive.drive(FORWARD)
    measure_distance()
    wait(1)
    reverse_lights()
    smartdrive.drive_for(REVERSE, 190, MM)
    default_lights()
    left_turn(87)
    place_in_box()
    right_turn(87)
    smartdrive.drive(FORWARD)
    smartdrive.set_drive_velocity(40, PERCENT)
    measure_distance_start()
    right_turn(87)

def _2a3b():
    claw_up()
    smartdrive.set_drive_velocity(40,PERCENT)
    smartdrive.drive(FORWARD)
    black_line()
    smartdrive.set_drive_velocity(40,PERCENT)
    smartdrive.drive_for(FORWARD, 300, MM)
    long_left_turn()
    wait(1)
    place_in_box()
    left_turn(87)
    claw_up()
    reverse_lights()
    smartdrive.drive_for(REVERSE, 320, MM)
    default_lights()
    left_turn(32)
    smartdrive.drive_for(FORWARD, 200, MM)
    claw_down()
    wait(1, SECONDS)
    left_turn(47)
    smartdrive.drive_for(FORWARD, 400, MM)
    place_in_box()
    smartdrive.drive_for(FORWARD, 30, MM)
    left_turn(95)
    smartdrive.set_drive_velocity(70)
    smartdrive.drive(FORWARD)
    measure_distance_start()
    reverse_lights()
    smartdrive.drive_for(REVERSE, 350, MM)
    default_lights()
    smartdrive.set_drive_velocity(40)
    left_turn(30)
    claw_up()
    smartdrive.drive_for(FORWARD, 220, MM)
    claw_down()
    stop()
    
place_holder_text()


#Main code:
#Choose between _2a3a(), _2a3b(), _2b3a(), or _2b3b(). _1c() and start() is required.
start()
_1c()
_2a3b()

