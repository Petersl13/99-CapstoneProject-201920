"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Lara Peters.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------

    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------

    root = tkinter.Tk()
    root.title('CSSE 120 Lara Peters, Winter 2018-19')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------

    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------

    #teleop_frame, arm_frame, control_frame, go_straight_frame, beep_frame, color_frame, go_straight, camera_frame, sprint_3 = get_shared_frames(main_frame, mqtt_sender)
    #color_frame, teleop_frame, go_straight, camera_frame, beep_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    sprint_3_frame = sprint_3_lara(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    #grid_frames(teleop_frame, arm_frame, control_frame, go_straight_frame, beep_frame, color_frame, go_straight, camera_frame, sprint_3)
    new_grid_frames(sprint_3_frame) #teleop_frame, color_frame, go_straight, camera_frame, beep_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()

def sprint_3_lara(window, mqtt_sender):
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
    frame_label = ttk.Label(frame, text='Sprint 3 Lara')
    frame_label.grid(row=0, column=0)

    warm_up_button = ttk.Button(frame, text='Warm-up')
    warm_up_button.grid(row=1, column=0)
    warm_up_button['command'] = lambda: handle_warm_up(mqtt_sender)

    speed_entry = ttk.Entry(frame, width=10)
    speed_label = ttk.Label(frame, text='Speed:')
    speed_entry.grid(row=1, column =2)
    speed_label.grid(row=0, column=2)

    area_label = ttk.Label(frame, text='Area(smaller than football area):')
    area_label.grid(row=2, column=2)
    area_entry = ttk.Entry(frame, width=10)
    area_entry.grid(row=3, column=2)


    spin_button = ttk.Button(frame, text='Take field')
    spin_button.grid(row=1, column=3)
    spin_button['command'] = lambda: handle_spin(mqtt_sender, speed_entry,area_entry)

    defender_button = ttk.Button(frame, text="Defender!")
    defender_button.grid(row=3, column = 0)
    defender_button['command'] = lambda: handle_defender(mqtt_sender,speed_entry)

    out_of_bounds_button = ttk.Button(frame, text='Out of bounds')
    out_of_bounds_button.grid(row=3, column=3)
    out_of_bounds_button['command'] = lambda: handle_out_of_bounds(mqtt_sender, )


    return frame


def get_shared_frames(main_frame, mqtt_sender):

    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    go_straight_frame = shared_gui.get_go_straight_frame(main_frame, mqtt_sender)
    beep_frame = shared_gui.beep_frame(main_frame, mqtt_sender)
    color_frame = shared_gui.colors(main_frame, mqtt_sender)
    go_straight = shared_gui.go_straight_until_frame(main_frame, mqtt_sender)
    camera_frame = shared_gui.camera_sensor_window(main_frame, mqtt_sender)
    sprint_3 = sprint_3_lara(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, go_straight_frame, beep_frame, color_frame, go_straight, camera_frame, sprint_3

def new_shared_frames(main_frame, mqtt_sender):

    sprint_3 = sprint_3_lara(main_frame, mqtt_sender)


    return sprint_3

def grid_frames(teleop_frame, arm_frame, control_frame, go_straight_frame, beep_frame, color_frame, go_straight, camera_frame, sprint_3):

    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=4, column=0)
    go_straight_frame.grid(row=0, column=1)
    beep_frame.grid(row=2, column=0)
    color_frame.grid(row=3, column=0)
    go_straight.grid(row=1, column=1)
    camera_frame.grid(row=2, column=1)
    sprint_3.grid(row=0, column=2, rowspan=5)

def new_grid_frames(sprint_3):

    sprint_3.grid(row=0, column=0)
    #teleop_frame.grid(row=1, column = 0)
    #color_frame.grid(row=2, column = 0)
    #go_straight.grid(row=3, column= 0)
    #camera_frame.grid(row=1, column=1)
    #beep_frame.grid(row=3, column=3)

def handle_warm_up(mqtt_sender):
    print('got warm up')
    mqtt_sender.send_message('warm_up')

def handle_spin(mqtt_sender, speed, area):
    print('got spin at speed', speed.get(), 'until I see football bigger than', area.get(),'then go at speed', speed,'until I pick up the ball')
    mqtt_sender.send_message('spin', [speed.get()])

def handle_defender(mqtt_sender, speed):
    print('got forward at speed', speed.get(),'until defender is there')
    mqtt_sender.send_message('go until defender', [speed.get()])

def handle_out_of_bounds(mqtt_sender, speed):
    print('got out of bounds')
    mqtt_sender.send_message('out of bounds', [speed.get()])




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
