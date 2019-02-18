
import rosebot
import time

def sound_as_approaches(robot,speed):

    start_time = 1.5
    beeper = robot.sound_system.beeper
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    robot.drive_system.go(speed, speed)
    while True:
        beeper.beep().wait()
        time.sleep(start_time)
        d_2 = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if d_2 < distance:
            distance = d_2
            start_time = start_time - 0.2
            if start_time < .1:
                start_time = .1
        if d_2 > distance:
            distance = d_2
            start_time = start_time + 0.2
        if d_2 <= 0.1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break

def spin_then_straight(robot, speed, area):
    robot.drive_system.spin_clockwise_until_sees_object(speed, area)
    sound_as_approaches(robot, speed)
