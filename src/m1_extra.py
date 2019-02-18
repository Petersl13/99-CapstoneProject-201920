
import rosebot

def sound_as_approaches(robot,speed):

    start_time = 1.5
    beeper = robot.sound_system.beeper
    distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    robot.drive_system.go(speed, speed)
    while True:
        beeper.beep().wait()
        d_2 = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if d_2 < distance:
            distance = d_2
            start_time = start_time - 0.2
        if d_2 > distance:
            distance = d_2
            start_time = start_time + 0.2
        if d_2 <= 0.2:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
