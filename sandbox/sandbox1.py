# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

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