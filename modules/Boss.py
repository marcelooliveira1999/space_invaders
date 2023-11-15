class Boss:
    hp_width = 100

    def __init__(self, turtle) -> None:
        self.turtle = turtle

    def create(self):
        self.turtle.register_shape("assets/img/Boss.gif")

        boss = self.turtle.Turtle()
        boss.shape("assets/img/Boss.gif")
        boss.speed(0)

        boss.up()
        boss.setposition(0, 240)

        return boss

    def move_boss(self, boss):
        if boss.xcor() < -240 or boss.xcor() > 240:
            boss.left(180)

        boss.forward(3)

    def hp_boss(self):
        hp = self.turtle.Turtle()

        hp.penup()
        hp.speed(0)

        hp.setposition(250, 280)

        hp.pensize(5)
        hp.color("red")

        hp.pendown()

        hp.left(180)
        hp.forward(100)

        hp.hideturtle()

        return hp

    def update_hp(self, boss, hp_boss, laser, sounds):
        self.hp_width -= 10

        hp_boss.clear()
        hp_boss.setx(250)

        if self.hp_width >= 10:
            hp_boss.forward(self.hp_width)
            return True

        elif self.hp_width < 10:
            hp_boss.clear()
            boss.hideturtle()

            laser.hideturtle()
            sounds.play_sound("explosion")

            return False
