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

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

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


    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(mqtt_sender,
        left_speed_entry, right_speed_entry)
    right_button["command"] = lambda: handle_right(mqtt_sender,
        left_speed_entry, right_speed_entry)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame

def get_go_straight_frame(window, mqtt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    frame.grid()
    frame_label = ttk.Label(frame, text='Go Straight For...')

    time_label = ttk.Label(frame, text='Time in Seconds:')
    time_entry = ttk.Entry(frame, width=8)

    inches_label = ttk.Label(frame, text='Inches:')
    inches_entry = ttk.Entry(frame, width=8)

    speed_entry = ttk.Entry(frame, width=8)
    speed_label = ttk.Label(frame, text='Speed:')
    speed_entry.grid(row=2, column=1)
    speed_label.grid(row=1, column=1)

    frame_label.grid(row = 0, column = 1)

    time_label.grid(row=1, column = 0)
    time_entry.grid(row=2, column = 0)

    inches_label.grid(row= 1, column= 2)
    inches_entry.grid(row= 2, column = 2)

    time_entry_button = ttk.Button(frame, text='Go for Time!')
    time_entry_button.grid(row=3, column=0)

    inches_entry_button = ttk.Button(frame, text="Go for Inches!")
    inches_entry_button.grid(row= 3, column=2)

    time_entry_button["command"] = lambda: handle_go_straight_for_seconds(mqtt_sender, time_entry, speed_entry)
    inches_entry_button["command"] = lambda:  handle_go_straight_for_inches(mqtt_sender, inches_entry, speed_entry)

    return frame

def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    #lower_warning_button = ttk.Button(frame, text='LOWER BUTTON WARNING')
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
    #lower_warning_button.grid(row=4, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    #lower_warning_button["command"] = lambda: print('Must have calibrated arm before use of *Lower arm* button!')
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

def beep_frame(window, mqtt_sender):
    """
        Constructs and returns a frame on the given window, where the frame has
        Button objects to exit this program and/or the robot's program (via MQTT).
          :type  window:       ttk.Frame | ttk.Toplevel
          :type  mqtt_sender:  com.MqttClient
        """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Sound")
    frame_label.grid(row=0, column=1)

    beep_entry = ttk.Entry(frame, width=8)
    beep_label = ttk.Label(frame, text='Number of Beeps:')
    tone_entry = ttk.Entry(frame, width=8)
    tone_label = ttk.Label(frame, text='Tone Frequency (800 - 1000):')
    tone_entry2 = ttk.Entry(frame, width=8)
    tone_label2 = ttk.Label(frame, text='Tone Duration (milliseconds):')
    speak_entry = ttk.Entry(frame, width=8)
    speak_label = ttk.Label(frame, text='What should I say?:')

    beep_button = ttk.Button(frame, text="Beep")
    tone_button = ttk.Button(frame, text="Tone")
    speak_button = ttk.Button(frame, text='Speak')

    beep_button.grid(row=2, column=1)
    beep_entry.grid(row=2, column=0)
    beep_label.grid(row=1, column=0)
    tone_button.grid(row=4, column=2)
    tone_entry.grid(row=4, column=0)
    tone_label.grid(row=3, column=0)
    tone_entry2.grid(row=4, column=1)
    tone_label2.grid(row=3, column=1)
    speak_label.grid(row=5, column=0)
    speak_entry.grid(row=6, column=0)
    speak_button.grid(row=6, column=1)

    beep_button["command"] = lambda: handle_beep(mqtt_sender, beep_entry)
    tone_button["command"] = lambda: handle_tone(mqtt_sender, tone_entry, tone_entry2)
    speak_button["command"] = lambda: handle_speak(mqtt_sender, speak_entry)

    return frame

def colors(window, mqtt_sender):
    """
            Constructs and returns a frame on the given window, where the frame has
            Button objects to exit this program and/or the robot's program (via MQTT).
              :type  window:       ttk.Frame | ttk.Toplevel
              :type  mqtt_sender:  com.MqttClient
            """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Colors!")
    frame_label.grid(row=0, column=0)

    speed_label = ttk.Label(frame, text='Speed:')
    speed_entry = ttk.Entry(frame, width=8)
    speed_label.grid(row=0, column=2)
    speed_entry.grid(row=1, column=2)

    go_to_intensityl_button = ttk.Button(frame, text='Go Until Intensity Less')
    intensity_entry = ttk.Entry(frame, width=8)
    intensity_label = ttk.Label(frame, text='Intensity:')

    go_to_intensityl_button.grid(row=2, column=0)
    intensity_label.grid(row=1, column=1)
    intensity_entry.grid(row=2, column=1)

    go_to_intensityl_button["command"] = lambda: handle_intensity(mqtt_sender, intensity_entry, speed_entry)

    go_to_intensityg_button = ttk.Button(frame, text='Go Until Intensity Greater')
    go_to_intensityg_button.grid(row=2, column=2)
    go_to_intensityg_button["command"] = lambda: handle_intensity_greater(mqtt_sender, intensity_entry, speed_entry)


    color_entry = ttk.Entry(frame, width=8)
    color_label = ttk.Label(frame, text='Color (int 0-7):')
    color_is_button = ttk.Button(frame, text='Color is?')
    color_is_not_button = ttk.Button(frame, text='Color is not?')

    color_entry.grid(row=4, column=1)
    color_label.grid(row=3, column=1)
    color_is_button.grid(row=4, column=0)
    color_is_not_button.grid(row=4, column=2)

    color_is_button["command"] = lambda: handle_color_is(mqtt_sender, color_entry, speed_entry)
    color_is_not_button["command"] = lambda: handle_color_is_not(mqtt_sender, color_entry, speed_entry)

    return frame

def go_straight_until_frame(window, mqtt_sender):
    """
                Constructs and returns a frame on the given window, where the frame has
                Button objects to exit this program and/or the robot's program (via MQTT).
                  :type  window:       ttk.Frame | ttk.Toplevel
                  :type  mqtt_sender:  com.MqttClient
                """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Proximity Sensor")
    frame_label.grid(row=0, column=1)

    speed_label = ttk.Label(frame, text='Speed:')
    speed_entry = ttk.Entry(frame, width=8)
    speed_label.grid(row=3, column=0)
    speed_entry.grid(row=4, column=0)

    distance_entry = ttk.Entry(frame, width=8)
    distance_label = ttk.Label(frame, text='Distance (inches):')
    distance_entry.grid(row=2, column=1)
    distance_label.grid(row=1, column=1)

    delta_entry = ttk.Entry(frame, width=8)
    delta_label = ttk.Label(frame, text='Delta (inches):')
    delta_entry.grid(row=4, column=2)
    delta_label.grid(row=3, column=2)

    until_distance_less_button = ttk.Button(frame, text='Go Forward (Until Less)')
    until_distance_greater_button = ttk.Button(frame, text='Go Backward (Until Greater)')
    until_distance_less_button.grid(row=2, column=0)
    until_distance_greater_button.grid(row=2, column=2)
    until_delta_button = ttk.Button(frame, text='Go Until Delta')
    until_delta_button.grid(row=3, column=1)

    until_distance_less_button["command"] = lambda: handle_distance_less(mqtt_sender, distance_entry, speed_entry)
    until_distance_greater_button["command"] = lambda: handle_distance_greater(mqtt_sender, distance_entry, speed_entry)
    until_delta_button["command"] = lambda: handle_delta_button(mqtt_sender, delta_entry, distance_entry, speed_entry)

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

    print('Forward:', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('forward', [left_entry_box.get(), right_entry_box.get()])

def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    print('Backward:', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('backward', [left_entry_box.get(), right_entry_box.get()])

def handle_left(mqtt_sender, left_entry_box, right_entry_box):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    print('Left:', int(left_entry_box.get()))
    mqtt_sender.send_message('left', [left_entry_box.get(), right_entry_box.get()])

def handle_right(mqtt_sender, left_entry_box, right_entry_box):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    print('Right:', int(right_entry_box.get()))
    mqtt_sender.send_message('right', [left_entry_box.get(), right_entry_box.get()])

def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Stop')
    mqtt_sender.send_message('stop', [])

def handle_beep(mqtt_sender, beep_entry):

    print('Beep:', beep_entry.get())
    mqtt_sender.send_message('beep', [beep_entry.get()])

def handle_tone(mqtt_sender, tone_entry, tone_entry2):

    print('Tone:', tone_entry.get(), tone_entry2.get())
    mqtt_sender.send_message('tone', [tone_entry.get(), tone_entry2.get()])

def handle_speak(mqtt_sender, speak_entry):

    print('Speak:', speak_entry.get())
    mqtt_sender.send_message('phrase', [speak_entry.get()])

def handle_go_straight_for_seconds(mqtt_sender, time, speed):

    print('Straight for seconds:', time.get(), 'At speed:', speed.get())
    mqtt_sender.send_message('straight_for_seconds', [time.get(), speed.get()])

def handle_go_straight_for_inches(mqtt_sender, inches, speed):

    print('Straight for inches:', inches.get(), 'At speed:', speed.get())
    mqtt_sender.send_message('straight_for_inches', [inches.get(), speed.get()])



###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Raise Arm')
    mqtt_sender.send_message('raise_arm', [])

def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Lower Arm')
    mqtt_sender.send_message('lower_arm', [])

def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Calibrate Arm')
    mqtt_sender.send_message('calibrate_arm', [])

def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('Move arm to position:', int(arm_position_entry.get()))
    mqtt_sender.send_message('move_arm_to_position', [arm_position_entry.get()])


def handle_intensity(mqtt_sender, intensity, speed):

    print('Intensity:', intensity.get(), 'At speed:', speed.get())
    mqtt_sender.send_message('go_straight_until_intensity_is_less_than', [intensity.get(), speed.get()])

def handle_intensity_greater(mqtt_sender, intensity, speed):

    print('Intensity:', intensity, 'At speed:', speed.get())
    mqtt_sender.send_message('go_straight_until_intensity_is_greater_than', [intensity.get(), speed.get()])

def handle_color_is(mqtt_sender, color, speed):

    print('Color:', color.get(), 'At speed:', speed.get())
    mqtt_sender.send_message('go_straight_until_color_is', [color.get(), speed.get()])

def handle_color_is_not(mqtt_sender, color, speed):

    print('Color:', color.get(), 'At speed', speed.get())
    mqtt_sender.send_message('go_straight_until_color_is_not', [color.get(), speed.get()])

def handle_distance_less(mqtt_sender, inches, speed):

    print('Distance:', inches.get(), 'At speed', speed.get())
    mqtt_sender.send_message('go_forward_until_distance_is_less_than', [inches.get(), speed.get()])

def handle_distance_greater(mqtt_sender, inches, speed):

    print('Distance:', inches.get(), 'At speed', speed.get())
    mqtt_sender.send_message('go_backward_until_distance_is_greater_than', [inches.get(), speed.get()])

def handle_delta_button(mqtt_sender, delta, inches, speed):

    print('Distance:', inches.get(), 'At speed', speed.get(), 'Within Distance:', delta)
    mqtt_sender.send_message('go_until_distance_is_within', [delta.get(), inches.get(), speed.get()])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('Quit')
    mqtt_sender.send_message('quit')

def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('Exit')
    handle_quit(mqtt_sender)
    exit()