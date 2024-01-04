from vex import *

distance = Distance(Ports.PORT8)
leftmotor=Motor(Ports.PORT7, False)
rightmotor=Motor(Ports.PORT12, True)
brain_inertial = Inertial()
brain_inertial.calibrate()
smartdrive=SmartDrive(leftmotor, rightmotor,brain_inertial)


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