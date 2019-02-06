from Quaternion import Quaternion
import sympy as sp


a = Quaternion(1.0, 2.0, 3.0, 4.0)
b = Quaternion(10.0, 20.0, 30.0, 40.0)

print(a)

print(a + b)

print(type(a))

# mul
print(a * 2)

#rmul
print(2 * a)

a * b

print(a.conjugate())
print(a.norm())
print(a.inverse())

print(a[0])

a[0] = -1.0

print(a)

q0, q1, q2, q3, p0, p1, p2, p3 = sp.symbols('q0 q1 q2 q3 p0 p1 p2 p3')

q = Quaternion(q0, q1, q2, q3)
p = Quaternion(p0, p1, p2, p3)

print(q + p)
print(3 * p)
print(q + a)
print(a == a)
