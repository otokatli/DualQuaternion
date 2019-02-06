import math as m

class Quaternion:
    def __init__(self, q0, q1, q2, q3):
        self.q0 = q0
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    def __str__(self):
        if isinstance(self.q0, float):
            return "Quaternion(%f, %f, %f, %f)" % (self.q0, self.q1, self.q2, self.q3)
        else:
            return "Quaternion(%s, %s, %s, %s)" % (self.q0, self.q1, self.q2, self.q3)

    def __getitem__(self, key):
        if key == 0:
            return self.q0
        elif key == 1:
            return self.q1
        elif key == 2:
            return self.q2
        elif key == 3:
            return self.q3
        else:
            print("Wrong key")

    def __setitem__(self, key, value):
        if key == 0:
            self.q0 = value
        elif key == 1:
            self.q1 = value
        elif key == 2:
            self.q2 = value
        elif key == 3:
            self.q3 = value
        else:
            print("Wrong key")
    
    def __add__(self, other):
        return Quaternion(self.q0 + other.q0, self.q1 + other.q1, self.q2 + other.q2, self.q3 + other.q3)

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            # implement quaternion multiplication
            pass
        else:
            return Quaternion(self.q0 * other, self.q1 * other, self.q2 * other, self.q3 * other)

    def __rmul__(self, other):
        if not isinstance(other, Quaternion):
            return Quaternion(self.q0 * other, self.q1 * other, self.q2 * other, self.q3 * other)

    def __truediv__(self, other):
        if not isinstance(other, Quaternion):
            return Quaternion(self.q0 / other, self.q1 / other, self.q2 / other, self.q3 / other)

    def conjugate(self):
        return Quaternion(self.q0, -self.q1, -self.q2, -self.q3)

    def norm(self):
        return m.sqrt(self.q0**2 + self.q1**2 + self.q2**2 + self.q3**2)

    def inverse(self):
        return self.conjugate() / self.norm()

    # might be useful
    def __dot(self, a, b):
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    def __cross(self, a, b):
        return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
