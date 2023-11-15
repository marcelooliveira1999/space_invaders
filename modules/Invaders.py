class Invaders:
    invaders = []

    def __init__(self, turtle, random, game_level) -> None:
        self.turtle = turtle
        self.random = random
        self.game_level = game_level

    def create_invader(self):
        self.turtle.register_shape("assets/img/invader.gif")

        for add_invaders in range(self.game_level["amount_invaders"]):
            self.invaders.append(self.turtle.Turtle())

        for invader in self.invaders:
            invader.shape("assets/img/invader.gif")
            invader.speed(0)

            invader.penup()

            invader_xcor = self.random.randint(-240, 240)
            invader_ycor = self.random.randint(140, 200)

            invader.setposition(invader_xcor, invader_ycor)

        return self.invaders

    def move_invader(self, invader):
        invader.left(180)

        invader_ycor = invader.ycor()
        invader_ycor -= self.game_level["advance_of_the_invaders"]

        invader.sety(invader_ycor)
