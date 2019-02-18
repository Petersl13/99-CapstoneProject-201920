# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

        """
        Goes forward or backward, repeated as necessary, until the robot is
        within the given delta of the given inches from the nearest object
        that it senses.  Assumes that it senses an object when it starts.

        For example, if delta is 0.3 and inches is 7.1, then
        the robot should move until it is between 6.8 and 7.4 inches
        from the object.
        """
        self.go(speed,speed)
        while True:
            if abs(self.sensor_system.ir_proximity_sensor.get_distance()) <= inches +- delta:
                self.stop()
                break
            if abs(self.sensor_system.ir_proximity_sensor.get_distance()) >= inches - delta:
                self.stop()
                break