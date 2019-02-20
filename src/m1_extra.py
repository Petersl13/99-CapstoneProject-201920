
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
        if d_2 <= 0.05:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break

def warm_up(robot):
    robot.calibrate_arm()
    robot.speech_maker('It is game time!')

def spin_then_straight(robot, speed, area):
    robot.drive_system.spin_clockwise_until_sees_object(speed, area)
    sound_as_approaches(robot, speed)

def go_forward_until_defender(robot, speed, inches_1, inches_2):
    robot.drive_system.go_forward_until_distance_is_less_than(inches_1, speed)
    robot.drive_system.go_backward_until_distance_is_greater_than(inches_2, speed)

def go_out_of_bounds(robot, left_speed, right_speed, shared_speed, intensity):
    robot.drive_system.go(left_speed, right_speed)
    robot.drive_system.go_straight_until_intensity_is_less_than(intensity, shared_speed)



