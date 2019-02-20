
import rosebot
import time

def sprint3(robot, speed):

    robot.drive_system.go(speed, speed)
    while True:

        color = robot.sensor_system.color_sensor.get_color()
        if color == 6:
            robot.drive_system.stop()
            trick_1(robot, speed)
            break
        if color == 3:
            robot.drive_system.stop()
            trick_2(robot, speed)
            break

def trick_1(robot, speed):

    robot.drive_system.spin_clockwise_until_sees_object(speed, 2)
    bark(robot)
    robot.drive_system.spin_counterclockwise_until_sees_object(speed, 2)
    bark(robot)
    robot.drive_system.spin_clockwise_until_sees_object(speed, 2)

def trick_2(robot, speed):

    robot.drive_system.spin_clockwise_until_sees_object(speed, 2)
    robot.arm_and_claw.calibrate_arm()
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    position = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    robot.drive_system.go(speed, speed)
    while True:
        d_2 = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if d_2 < distance:
            distance = d_2
        if d_2 > distance:
            distance = d_2
        if d_2 <= 0.1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            robot.drive_system.go_straight_for_inches_using_time(position, -speed)
            robot.arm_and_claw.lower_arm()
            break
    bark(robot)

def bark(robot):

    robot.sound_system.speech_maker.speak('bark').wait()