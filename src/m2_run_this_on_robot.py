"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Nathalie Grier.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time

robot = rosebot.RoseBot()

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """

    #run_test_arm_raise()
    run_test_arm_raise()

def run_test_arm_raise():

    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.calibrate_arm()

def run_test_arm_lower():

    robot.arm_and_claw.lower_arm()



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()