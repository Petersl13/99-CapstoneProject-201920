"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Nathalie Grier.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

robot = rosebot.RoseBot()

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_thing()
    #run_test_arm_raise()
    #run_test_arm_lower()
    #run_test_go()

def real_thing():

    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate.is_time_to_stop:
            break

def run_test_arm_raise():

    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.calibrate_arm()

def run_test_arm_lower():

    robot.arm_and_claw.lower_arm()

def run_test_go():

    robot.drive_system.go(left_wheel_speed=100, right_wheel_speed=100)
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_seconds(5, 50)
    robot.drive_system.go_straight_for_inches_using_time(10, 100)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()