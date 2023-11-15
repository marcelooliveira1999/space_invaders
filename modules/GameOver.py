class Game_over:

    def __init__(self, turtle, window, time) -> None:
        self.turtle = turtle
        self.window = window
        self.time = time

    def lose(self):
        lose = self.turtle.Turtle()

        lose.color("red")
        lose.penup()

        lose.write("GAME OVER", align="center", font=("Arial", 50, "normal"))
        lose.hideturtle()

        self.time.sleep(3)
        self.window.bye()
