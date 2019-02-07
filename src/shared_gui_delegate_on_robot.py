"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Lara Peters and Nathalie Grier.
  Winter term, 2018-2019.
"""
class Handler(object):
    def __init__(self, robot):
        """
        :type robot: rosebot.Rosebot
        """
        self.robot = robot

    def forward(self, left_wheel_speed, right_wheel_speed):
        print('got forward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def backward(self, left_wheel_speed, right_wheel_speed):
        print('got backward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))


    def left(self, left_wheel_speed):
        print('got left', left_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed))


    def right(self, right_wheel_speed):
        print('got right', right_wheel_speed)
        self.robot.drive_system.go( int(right_wheel_speed))



    def stop(self):
        self.robot.drive_system.stop()

