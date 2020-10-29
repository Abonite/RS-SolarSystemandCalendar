import math

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

def Distance(star_1, star_2):
    """
    caculate the distance of two stars in 3D
    """
    d = [0, 0, 0]

    d[0] = abs(star_1.p_x - star_2.p_x)
    d[1] = abs(star_1.p_y - star_2.p_y)
    d[2] = abs(star_1.p_z - star_2.p_z)

    return d

def Accelerate(star_1, star_2, choos):
    """
    caculate the accelerate of one stars in 3D
    """
    #gravitational constant
    G = 6.6725 * pow(10 , -11)

    a = [0, 0, 0]
    
    d = Distance(star_1, star_2)

    if choos == 0:
        a[0] = G * star_2 / d[0]
        a[1] = G * star_2 / d[1]
        a[2] = G * star_2 / d[2]

    elif choos == 1:
        a[0] = G * star_1 / d[0]
        a[1] = G * star_1 / d[1]
        a[2] = G * star_1 / d[2]

    else:
        print("加速度计算输入参数错误")
        exit()

    return a

def Velocity(star_1, star_2, t):
    """
    caculate the velocity of one stars
    """
    a_1 = Accelerate(star_1, star_2, 0)
    a_2 = Accelerate(star_1, star_2, 1)

    star_1.V_x = star_1.V_x + a_1[0] * t
    star_1.V_y = star_1.V_y + a_1[1] * t
    star_1.V_z = star_1.V_z + a_1[2] * t

    star_2.V_x = star_2.V_x + a_2[0] * t
    star_2.V_y = star_2.V_y + a_2[1] * t
    star_2.V_z = star_2.V_z + a_2[2] * t

def Place(star_1, star_2, t):
    """
    caculate the nwe place
    """
    a = Accelerate(star_1, star_2)

    star_1.p_x = star_1.p_x * t + 0.5 * a[0] * pow(t ,2)
    star_1.p_y = star_1.p_y * t + 0.5 * a[1] * pow(t ,2)
    star_1.p_z = star_1.p_z * t + 0.5 * a[2] * pow(t ,2)

    star_1.p_x = star_1.p_x * t + 0.5 * a[0] * pow(t ,2)
    star_1.p_y = star_1.p_y * t + 0.5 * a[1] * pow(t ,2)
    star_1.p_z = star_1.p_z * t + 0.5 * a[2] * pow(t ,2)

if __name__ == "__main__":
    #               -   velocity    - accelerated -    place         -      mass    -
    Sun = Stars     (0, 0, 0,           0, 0, 0,      0, 0, 0,              1.9891e30)
    Earth = Stars   (0, 29783000, 0,    0, 0, 0,      1.496e11, 1, 1,       5.965e24)
    Kas = Stars     (0, 1023, 0,        0, 0, 0,      149994950000, 2, 2,   7.349e22)

    t = 10

    while True:
        print("The Sun:")
        print(Sun.p_x)
        print(Sun.p_y)
        print(Sun.p_z)
        print("The Earth:")
        print(Earth.p_x)
        print(Earth.p_y)
        print(Earth.p_z)