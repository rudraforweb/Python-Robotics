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
pusher = Motor(Ports.PORT8, True)
pusher.set_max_torque(100, PERCENT)
brain.screen.print("Claw motor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
brain.screen.print("Touchleds good!")
wait(0.2, SECONDS)
brain.screen.next_row()
color =ColorSensor(Ports.PORT1)
light =ColorSensor(Ports.PORT3)
light.set_light(100, PERCENT)
color.set_light(100, PERCENT)
brain.screen.print("Color sensor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
distance = Distance(Ports.PORT11)
brain.screen.print("Distance sensor good!")
wait(0.2, SECONDS)
brain.screen.next_row()
brain.battery.capacity()
brain.screen.print("Battery good!")                 
wait(1, SECONDS)
brain.screen.clear_screen()
#End of "system check".

#Define functions:
claw_up_degrees = 50
claw_down_degrees = 5

bit_1 = 0
bit_2 = 0
bit_3 = 0

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
    touchledleft.set_brightness(100)
def blink_orange_right():
    touchledright.set_brightness(100)
    touchledright.set_color(Color.YELLOW_ORANGE)
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
def long_right_turn(turn):
    touchledleft.set_brightness(100)
    touchledleft.set_color(Color.WHITE)
    blink_orange_right()
    leftmotor.spin_for(FORWARD, turn, DEGREES)
    leftmotor.stop()
    touchledleft.set_brightness(0)
    touchledright.set_brightness(0)
def long_left_turn(turn):
    touchledright.set_brightness(100)
    touchledright.set_color(Color.WHITE)
    blink_orange_left()
    leftmotor.spin_for(REVERSE, turn, DEGREES)
    leftmotor.stop()
    touchledleft.set_brightness(0)
    touchledright.set_brightness(0)

#Measure distances:
def measure_distance_start():
    while distance.object_distance(INCHES) < 2: 
        wait(0.1, SECONDS)
        smartdrive.set_drive_velocity(40, PERCENT)
        if distance.object_distance(INCHES) > 2: #type: ignore
            smartdrive.drive_for(FORWARD, 65, MM)
            stop()
            break
def measure_distance():
    while distance.object_distance(INCHES) < 2:
        wait(0.1, SECONDS)
        if distance.object_distance(INCHES) > 2: #type: ignore
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
        if distance.object_distance(INCHES) > 2: #type: ignore
            stop()
            reverse_lights()
            smartdrive.drive_for(REVERSE, 50, MM)
            default_lights()
            break 
def right_measure_distance(right_measure, reverse_measure):
    smartdrive.drive(FORWARD)
    while distance.object_distance(INCHES) < 2:
            wait(0.1, SECONDS)
            smartdrive.set_drive_velocity(40, PERCENT)
            if distance.object_distance(INCHES) > 2: #type: ignore
                stop()
                smartdrive.drive_for(REVERSE, reverse_measure, MM)
                leftmotor.spin_for(FORWARD, right_measure, DEGREES)
                stop()
                break
def left_measure_distance(left_measure, reverse_measure):
    smartdrive.drive(FORWARD)
    while distance.object_distance(INCHES) < 2:
            wait(0.1, SECONDS)
            smartdrive.set_drive_velocity(40, PERCENT)
            if distance.object_distance(INCHES) > 2: #type: ignore
                stop()
                smartdrive.drive_for(REVERSE, reverse_measure, MM)
                rightmotor.spin_for(FORWARD, left_measure, DEGREES)
                stop()
                break

#Others:
def place_holder_text():
    brain.screen.clear_screen()
    brain.screen.set_font(FontType.PROP30)
    brain.screen.set_cursor(2, 2)
    brain.screen.print("  Python-Robotics")    
def black_line():
    while int(color.brightness()) >= 25: #type: ignore
        wait(0.1, SECONDS)
        smartdrive.set_stopping(HOLD)
        if int(color.brightness()) <= 25: #type: ignore 
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
def start(): #Good
    claw_up()
    if int(color.brightness()) <= 50: #type: ignore 
        wait(0.1, SECONDS)
        stop()
        brain.screen.set_cursor(1,1)
        brain.screen.print("Bit 1: Black")
        bit_1 = 1
        smartdrive.drive(FORWARD)
    else:
        brain.screen.set_cursor(1,1)
        brain.screen.print("Bit 1: White")
        bit_1 = 0


    smartdrive.drive_for(FORWARD, 45, MM)


    if int(color.brightness()) <= 50: #type: ignore 
            wait(0.1, SECONDS)
            stop()
            brain.screen.set_cursor(2,1)
            brain.screen.print("Bit 2: Black")
            bit_2 = 1
            smartdrive.drive(FORWARD)
    else:
        brain.screen.set_cursor(2,1)
        brain.screen.print("Bit 2: White")
        bit_2 = 0

    smartdrive.drive_for(FORWARD, 45, MM)

    if int(color.brightness()) <= 50: #type: ignore 
            wait(0.1, SECONDS)
            stop()
            brain.screen.set_cursor(3,1)
            brain.screen.print("Bit 3: Black")
            bit_3 = 1
            stop()

    else:
        brain.screen.set_cursor(3,1)
        brain.screen.print("Bit 3: White")
        bit_3 = 0
        stop()
    
    smartdrive.drive_for(FORWARD, 45, MM)

    right_turn(88)

def food_ball(): #Good
    smartdrive.set_drive_velocity(60)
    smartdrive.drive_for(REVERSE, 29, INCHES)

def game_ending_task():
    #place code here for the game ending task.
    #The bits are named: bit_1, bit_2, and bit_3.
    wait(1)
    brain.screen.set_cursor(5,1)
    brain.screen.print(bit_1 + bit_2 + bit_3 + 3)

#1:
def _1c(): #Good
    #Collect 1:
    smartdrive.drive(FORWARD)
    right_measure_distance(445, 65)
    smartdrive.set_drive_velocity(40,PERCENT)
    smartdrive.drive(FORWARD)
    black_line()
    smartdrive.drive_for(FORWARD, 100, MM)
    #Place 1 in C:
    right_measure_distance(440, 137)
    smartdrive.set_turn_velocity(20, PERCENT)
    smartdrive.drive(FORWARD)
    measure_distance()
    wait(1)
    reverse_lights()
    smartdrive.drive_for(REVERSE, 195, MM)
    default_lights()
    left_turn(91)
    place_in_box()
    #Go for 2:
    right_turn(89)
    smartdrive.drive(FORWARD)
    smartdrive.set_drive_velocity(40, PERCENT)

#2:       
def _2a(): #Good
    #Collect 2:
    right_measure_distance(442, 80)
    claw_up()
    smartdrive.set_drive_velocity(40,PERCENT)
    smartdrive.drive(FORWARD)
    black_line()
    #Place 2 in A:
    smartdrive.set_drive_velocity(40,PERCENT)
    smartdrive.drive_for(FORWARD, 330, MM)
    long_left_turn(425)
    wait(1)
    place_in_box()
    food_ball()
    
    
def _2b(): #Good
    #Collect 2:
    right_measure_distance(440, 90)
    claw_up()
    smartdrive.set_drive_velocity(40,PERCENT)
    smartdrive.drive(FORWARD)
    black_line()
    smartdrive.set_drive_velocity(40,PERCENT)
    smartdrive.drive_for(FORWARD, 320, MM)
    long_left_turn(418)
    wait(1)
    smartdrive.set_drive_velocity(20,PERCENT)
    food_ball()
    #Place 2 into b:
    smartdrive.drive(FORWARD)
    measure_distance_c()
    right_turn(88)
    smartdrive.drive_for(REVERSE, 210, MM)
    leftmotor.spin_for(FORWARD, 419, DEGREES)
    smartdrive.drive(FORWARD)
    measure_distance_c()
    place_in_box()
    #Go into 3 position:
    left_turn(80)
    smartdrive.drive_for(REVERSE, 170, MM)
    rightmotor.spin_for(FORWARD, 436, DEGREES)

def _2c(): #Good
    #Collect 2:
    right_measure_distance(430, 80)
    claw_up()
    smartdrive.set_drive_velocity(40,PERCENT)
    smartdrive.drive(FORWARD)
    black_line()
    #Place 2 into C:
    smartdrive.drive_for(REVERSE, 6, INCHES)
    long_left_turn(418)
    left_turn(94)
    left_measure_distance(445, 150)
    smartdrive.drive(FORWARD)
    measure_distance()
    reverse_lights()
    smartdrive.drive_for(REVERSE, 200, MM)
    default_lights()
    right_turn(88)
    place_in_box()
    #Food ball:
    right_turn(88)
    right_measure_distance(446, 77)
    claw_up()
    smartdrive.drive(FORWARD)
    while int(color.brightness()) >= 25: #type: ignore
        wait(0.1, SECONDS)
        smartdrive.set_stopping(HOLD)
        if int(color.brightness()) <= 25: #type: ignore 
            wait(0.1, SECONDS)
            stop()
            wait(1, SECONDS)
            break
    smartdrive.set_drive_velocity(40,PERCENT)
    smartdrive.drive_for(FORWARD, 360, MM)
    long_left_turn(427)
    wait(1)
    smartdrive.set_drive_velocity(15,PERCENT)
    food_ball()
    
#3:
def _3a(): #Good
    #Collect 3:
    right_measure_distance(425, 116)
    pusher.spin_to_position(2, DEGREES)
    smartdrive.set_drive_velocity(100)
    smartdrive.drive_for(FORWARD, 40, INCHES)
    left_turn(88)
    long_right_turn(430)
    smartdrive.set_drive_velocity(70)
    claw_up()
    right_measure_distance(430, 50)
    smartdrive.set_drive_velocity(30)
    smartdrive.drive_for(FORWARD, 150, MM)
    claw_down()
    #Place 3 in A:
    right_measure_distance(440, 80)
    smartdrive.set_drive_velocity(50)
    smartdrive.drive(FORWARD)
    while int(color.brightness()) >= 25: #type: ignore
        wait(0.1, SECONDS)
        smartdrive.set_stopping(HOLD)
        if int(color.brightness()) <= 25: #type: ignore 
            wait(0.1, SECONDS)
            stop()
            wait(1, SECONDS)
            break
    smartdrive.drive_for(FORWARD, 360, MM)
    right_turn(88)
    smartdrive.drive(FORWARD)
    measure_distance()
    place_in_box()
    stop()    

def _3b(): #Good
    #Collect 3:
    right_measure_distance(425, 116)
    pusher.spin_to_position(2, DEGREES)
    smartdrive.set_drive_velocity(100)
    smartdrive.drive_for(FORWARD, 40, INCHES)
    left_turn(88)
    long_right_turn(430)
    smartdrive.set_drive_velocity(70)
    claw_up()
    right_measure_distance(430, 50)
    smartdrive.set_drive_velocity(30)
    smartdrive.drive_for(FORWARD, 150, MM)
    claw_down()
    #Place 3 in B:
    right_turn(179)
    left_measure_distance(420, 80)
    smartdrive.set_drive_velocity(50)
    smartdrive.drive(FORWARD)
    while int(color.brightness()) >= 25: #type: ignore
        wait(0.1, SECONDS)
        smartdrive.set_stopping(HOLD)
        if int(color.brightness()) <= 25: #type: ignore 
            wait(0.1, SECONDS)
            stop()
            wait(1, SECONDS)
            break
    smartdrive.drive_for(FORWARD, 260, MM)
    left_turn(88)
    smartdrive.drive(FORWARD)
    measure_distance()
    stop()
    place_in_box()
    stop()
    
def _3c(): #Good
    #Collect 3:
    right_measure_distance(425, 114)
    pusher.spin_to_position(2, DEGREES)
    smartdrive.set_drive_velocity(100)
    smartdrive.drive_for(FORWARD, 40, INCHES)
    left_turn(88)
    long_right_turn(430)
    smartdrive.set_drive_velocity(70)
    claw_up()
    right_measure_distance(430, 50)
    smartdrive.set_drive_velocity(30)
    smartdrive.drive_for(FORWARD, 150, MM)
    claw_down()
    #Place 3 in C:
    right_measure_distance(440, 80)
    smartdrive.set_drive_velocity(70)
    smartdrive.drive(FORWARD)
    while int(color.brightness()) >= 25: #type: ignore
        wait(0.1, SECONDS)
        smartdrive.set_stopping(HOLD)
        if int(color.brightness()) <= 25: #type: ignore 
            wait(0.1, SECONDS)
            stop()
            wait(1, SECONDS)
            break
    smartdrive.set_drive_velocity(30, PERCENT)
    right_measure_distance(445, 100)
    smartdrive.set_turn_velocity(20, PERCENT)
    smartdrive.drive(FORWARD)
    measure_distance()
    wait(1)
    reverse_lights()
    smartdrive.drive_for(REVERSE, 170, MM)
    default_lights()
    left_turn(94)
    place_in_box()
    right_turn(94)



#Instructions:
#Choose between _2a(), _2b(), _3a(), _3b(), 2c(), and 3c() in the right order.
#_1c() and start() is required. DO NOT put in food_ball().
#Edit game_ending_task() to your own free will.

#Main code:
start()
_1c()
_2b()
_3c()
game_ending_task()

