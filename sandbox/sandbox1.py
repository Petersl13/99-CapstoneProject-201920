# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Lara Peters and Nathalie Grier.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    beep_entry = ttk.Entry(frame, width=8)
    beep_label = ttk.Label(frame, text='Number of Beeps:')
    tone_entry = ttk.Entry(frame, width=8)
    tone_label = ttk.Label(frame, text='Tone Frequency:')
    tone_entry2 = ttk.Entry(frame, width=8)
    tone_label2 = ttk.Label(frame, text='Tone Duration (milliseconds):')

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")
    beep_button = ttk.Button(frame, text="Beep")
    tone_button = ttk.Button(frame, text="Tone")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    beep_button.grid(row=7, column=1)
    beep_entry.grid(row=7, column=0)
    beep_label.grid(row=6, column=0)
    tone_button.grid(row=9, column=2)
    tone_entry.grid(row=9, column=0)
    tone_label.grid(row=8, column=0)
    tone_entry2.grid(row=9, column=1)
    tone_label2.grid(row=8, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)
    beep_button["command"] = lambda: handle_beep(mqtt_sender, beep_entry)
    tone_button["command"] = lambda: handle_tone(mqtt_sender, tone_entry, tone_entry2)

    return frame

def go_straight_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, releif='ridge')
    frame.grid()
    frame_label = ttk.Label(frame, text='Go Straight For...')
    time_label = ttk.Label(frame, text='Time in Seconds')
    time_entry = ttk.Entry(frame, width=8)
    inches_label = ttk.Label(frame, text='Inches')
    inches_entry = ttk.Entry(frame, width=8)
    frame_label.grid(row = 0, column = 1)
    time_label.grid(row=1, column = 0)
    time_entry.grid(row=2, column = 0)
    inches_label.grid(row= 1, column= 1)
    inches_entry.grid(row= 2, column = 1)
    time_entry_button = ttk.Button(frame, text='time')
    time_entry_button.grid(row=3, column=0)
    inches_entry_button = ttk.Button(frame, text="inches")
    inches_entry_button.grid(row= 3, column=1)
    time_entry_button["command"] = lambda: handle_go_straight_for_seconds(seconds, mqtt_sender)
    inches_entry_button["command"] = lambda:  handle_go_straight_for_inches(mqtt_sender,inches)


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    print('forward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('forward', [left_entry_box.get(), right_entry_box.get()])

def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    print('backward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('backward', [left_entry_box.get(), right_entry_box.get()])

def handle_left(left_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    print('left', left_entry_box.get())
    mqtt_sender.send_message('left', [left_entry_box.get()])

def handle_right(right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    print('right', right_entry_box.get())
    mqtt_sender.send_message('right', [right_entry_box.get()])

def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('stop')
    mqtt_sender.send_message('stop', [])

def handle_beep(mqtt_sender, beep_entry):

    print('beep', int(beep_entry.get()))
    mqtt_sender.send_message('beep', [beep_entry.get()])


def handle_tone(mqtt_sender, tone_entry, tone_entry2):

    print('tone', int(tone_entry.get()), int(tone_entry2.get()))
    mqtt_sender.send_message('tone', [int(tone_entry.get()), int(tone_entry2.get())])

def handle_go_straight_for_seconds(mqtt_sender, time_entry):
    print('go straight for seconds')
    mqtt_sender.send_message('go_straight_for_seconds', [int(time_entry.get())])

def handle_go_straight_for_inches(mqtt_sender, inches_entry):
    print('go straight for inches')
    mqtt_sender.send_message('go_straight_for_inches', [int(inches_entry.get())])



###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit')

def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()




def go(self, speed, inches, delta):
        while True:

            if self.sensor_system.ir_proximity_sensor.get_distance_in_inches() < inches - delta:
                self.go(-speed, -speed)
                if self.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= inches- delta:
                    self.stop()
                    break
            if self.sensor_system.ir_proximity_sensor.get_distance_in_inches() > inches + delta:
                self.go(speed, speed)
                if self.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= inches + delta:
                    self.stop()
                    break


def warm_up(self):
    print('Got warm up from m1_extra')
    m1_extra.warm_up(self)


def spin(self, speed, area):
    print('Got spin from m1_extra')
    m1_extra.spin_then_straight(self, speed, area)
