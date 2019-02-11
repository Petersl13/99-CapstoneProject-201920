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
        self.is_time_to_stop = False

    def forward(self, left_wheel_speed, right_wheel_speed):
        print('got forward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def backward(self, left_wheel_speed, right_wheel_speed):
        print('got backward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))


    def left(self, left_wheel_speed, right_wheel_speed):
        print('got left', left_wheel_speed)
        right_wheel_speed = 0
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))


    def right(self, left_wheel_speed ,right_wheel_speed):
        print('got right', right_wheel_speed)
        left_wheel_speed = 0
        self.robot.drive_system.go(left_wheel_speed, int(right_wheel_speed))




    def stop(self):
        self.robot.drive_system.stop()


    def quit(self):
        print('got quit')
        self.is_time_to_stop = True



    def beep(self, n):
        print('got beep')
        for k in range(n+1):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, f, t):
        print('got tone')
        self.robot.sound_system.tone_maker.tone(f, t).wait()

    def phrase(self, p):
        print('got phrase')
        self.robot.sound_system.speech_maker.speak(p).wait()


    print("I will beep N times")
    print('I will play tone at frequency F for the durration T')
    print('I will speak phsrase P')