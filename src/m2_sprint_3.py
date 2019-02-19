
import rosebot
import time

def sprint3(robot, speed):

    robot.drive_system.go(speed, speed)
    while True:
        if robot.color_system.get_color() == 4: #yellow
            robot.drive_system.stop()
            trick_1(robot, speed)
            break
        if robot.color_system.get_color() == 2: #blue
            robot.drive_system.stop()
            trick_2(robot, speed)
            break
        if robot.proximity_sensor.get_distance_in_inches() <= 5:
            robot.drive_system.stop()
            bark(robot)
            break

def trick_1(robot, speed): #spin

    robot.drive_system.spin_clockwise_until_sees_area(speed, 2) #train to block/me
    bark(robot)
    robot.drive_system.spin_counterclockwise_until_sees_area(speed, 2)
    bark(robot)
    robot.drive_system.spin_clockwise_until_sees_area(speed, 2)

def trick_2(robot, speed):

    robot.drive_system.spin_clockwise_until_sees_area(speed, 2)
    robot.arm_and_claw.calibrate_arm()
    position = robot.proximity_sensor.get_distance_in_inches()
    robot.drive_system.go(speed, speed)
    while True:
        if robot.proximity_sensor.get_distance_in_inches() <= 0.02:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            robot.drive_system.go_straight_for_inches_using_time(position, -speed)
            robot.arm_and_claw.lower_arm()
            bark(robot)
            break

def bark(robot):

    robot.speech_maker('bark')
    robot.speech_maker('bark')