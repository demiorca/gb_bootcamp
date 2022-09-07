import turtle


def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ''
    for _ in range(iters):
        end_string = ''.join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)


def main(iterations, axiom, rules, angle, length=8, size=2, y_offset=0,
         x_offset=0, offset_angle=0, width=800, height=800):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    t.up()
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length)
    t.hideturtle()

    wn.exitonclick()


# Снежинка Коха
# axiom = 'F--F--F'
# rules = {'F': 'F+F--F+F'}
# iterations = 3
# angle = 60

# Квадратный остров Коха
# axiom = 'F+F+F+F'
# rules = {'F': 'F-F+F+FFF-F-F+F'}
# iterations = 2
# angle = 90

# Ковёр Серпинского
# axiom = 'YF'
# rules = {'X': 'YF+XF+Y', 'Y': 'XF-YF-X'}
# iterations = 5
# angle = 60

# Решётка Серпинского
# axiom = 'FXF--FF--FF'
# rules = {'F': 'FF', 'X': '--FXF++FXF++FXF--'}
# iterations = 4
# angle = 60

# Кривая Серпинского
axiom = "F+XF+F+XF"
rules = {"X":"XF-F+F-XF+F+XF-F+F-X"}
iterations = 3
angle = 90

if __name__ == '__main__':
    main(iterations, axiom, rules, angle)
