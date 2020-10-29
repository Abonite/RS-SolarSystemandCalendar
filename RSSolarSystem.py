import numpy as np

class Stars:
    def __init__(self, V_x, V_y, V_z, a_x, a_y, a_z, p_x, p_y, p_z, m):
        """
        V is Velocity
        a is accelerate
        p is place
        m is mass
        """
        self.V_x = V_x
        self.V_y = V_y
        self.V_z = V_z

        self.a_x = a_x
        self.a_y = a_y
        self.a_z = a_z

        self.m = m

        self.p_x = p_x
        self.p_y = p_y
        self.p_z = p_z

