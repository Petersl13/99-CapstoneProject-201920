"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Lara Peters and Nathalie Grier.
  Winter term, 2018-2019.
"""
import rosebot
import m1_extra
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

    def raise_arm(self):
        print('got raise arm')
        self.robot.arm_and_claw.raise_arm()

    def calibrate_arm(self):
        print('got calibrate arm')
        self.robot.arm_and_claw.calibrate_arm()

    def lower_arm(self):
        print('got lower arm')
        self.robot.arm_and_claw.lower_arm()

    def move_arm_to_position(self, n):
        print('got move arm to position')
        self.robot.arm_and_claw.move_arm_to_position(int(n))



    def stop(self):

        self.robot.drive_system.stop()


    def quit(self):

        print('got quit')
        self.is_time_to_stop = True



    def beep(self, beep_entry):

        print('got beep')
        for k in range(int(beep_entry)):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, f, t):

        print('got tone')
        self.robot.sound_system.tone_maker.play_tone(int(f), int(t)).wait()

    def phrase(self, p):

        print('got phrase')
        self.robot.sound_system.speech_maker.speak(str(p)).wait()

    def straight_for_seconds(self, seconds, speed):

        print('got striaght for seconds', seconds, 'at speed', speed)
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def straight_for_inches(self, inches, speed):

        print('got straight for inches', inches, 'at speed', speed)
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def go_straight_until_intensity_is_less_than(self, intensity, speed):
        print('got intensity', intensity, 'at speed', speed)
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity), int(speed))

    def go_straight_until_intensity_is_greater_than(self, intensity, speed):
        print('got intensity', intensity, 'at speed', speed)
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity), int(speed))
        
    def go_straight_until_color_is(self, color, speed):
        print('got straight until color is', color, 'at speed', speed)
        self.robot.drive_system.go_straight_until_color_is(int(color), int(speed))


    def go_straight_until_color_is_not(self, color, speed):
        print('got straight until color is', color, 'at speed', speed)
        self.robot.drive_system.go_straight_until_color_is_not(int(color), int(speed))

    def go_forward_until_distance_is_less_than(self, inches, speed):
        print('got straight until distance is less than', inches, 'at speed', speed)
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches), int(speed))

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        print('got backward until distance is greater than', inches, 'at speed', speed)
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches), int(speed))

    def go_until_distance_is_within(self, delta, inches, speed):
        print('got go distance until delta', delta, inches, speed)
        self.robot.drive_system.go_until_distance_is_within(int(delta), int(inches), int(speed))

    def spin_clockwise_until_sees_object(self, speed, area):
        print('got clockwise until sees object bigger than', area, 'at speed', speed)
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def spin_counterclockwise_until_sees_object(self, speed, area):
        print('got counterclockwise until sees object bigger than', area, 'at speed', speed)
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed) , int(area))

    def sound_as_approaches(self,speed):
        print('got sound as approaches at speed', speed)
        m1_extra.sound_as_approaches(self.robot, speed)

        
    def spin_then_straight(self, speed):
        print('got spin then straight at speed', speed)
        m1_extra.spin_then_straight(self.robot, speed)

