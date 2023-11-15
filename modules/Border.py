class Border:

    def __init__(self, turtle) -> None:
        self.turtle = turtle

    def create_border(self):
        border = self.turtle.Turtle()

        border.color('gray')
        border.speed(0)

        border.up()
        border.setposition(-250, -250)

        border.pensize(3)
        border.down()

        for write_border in range(4):
            border.forward(500)
            border.left(90)

        border.hideturtle()

    def add_background(self):
        self.turtle.register_shape("assets/img/background.gif")

        background = self.turtle.Turtle()
        background.shape("assets/img/background.gif")
        background.speed(0)

        background.up()
        background.setposition(0, 0)
