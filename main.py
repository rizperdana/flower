import turtle

t = turtle.Turtle()
turtle.bgcolor('#1D263B')

for i in range(180):
    t.speed(0)
    t.color('#F9A03F')
    t.circle(190 - i, 90)
    t.left(90)
    t.color('#F7D488')
    t.circle(190 - 1, 90)
    t.left(18)
