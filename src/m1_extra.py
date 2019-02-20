
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
    robot.arm_and_claw.calibrate_arm()
    robot.sound_system.speech_maker.speak('It is game time!')

def spin_then_straight(robot, speed, area):
    robot.drive_system.spin_clockwise_until_sees_object(speed, area)
    sound_as_approaches(robot, speed)

def go_forward_until_defender(robot, speed):
    robot.drive_system.go_forward_until_distance_is_less_than(4, speed)
    robot.drive_system.go_backward_until_distance_is_greater_than(6, speed)

def go_out_of_bounds(robot, shared_speed):
    robot.drive_system.go(60, 50)
    robot.drive_system.go_straight_until_intensity_is_less_than(3, shared_speed)

def score(robot, speed):
    robot.drive_system.go(speed, speed)
    #while True:
    robot.drive_system.go_straight_until_intensity_is_greater_than(90)
    robot.drive_system.stop()
    robot.sound_system.speech_maker.speak('Touchdown!')
    robot.arm_and_claw.lower_arm()
            #break




