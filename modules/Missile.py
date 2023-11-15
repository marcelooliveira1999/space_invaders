class Missile:
    missile = False
    missile_state = "ready"

    def __init__(self, turtle, player, sounds) -> None:
        self.turtle = turtle
        self.player = player
        self.sounds = sounds

    def create_missile(self):
        self.missile = self.turtle.Turtle()
        self.missile.hideturtle()

        self.missile.shape("circle")
        self.missile.color("yellow")

        self.missile.shapesize(0.5)
        self.missile.speed(0)

        self.missile.up()
        self.missile.setheading(90)

        return self.missile

    def shoot_missile(self):
        if self.missile_state == "ready":
            self.missile_state = "fire"

            x_cor = self.player.xcor()
            y_cor = self.player.ycor()

            self.missile.setposition(x_cor, y_cor + 20)
            self.sounds.play_sound("shoot")

    def check_missile_status(self):
        if self.missile_state == "ready":
            return False
        elif self.missile_state == "fire":
            return True

    def check_missile_position(self, moviment=False, reload=False):
        if moviment and self.missile.ycor() < 240:
            return True

        if reload and self.missile.ycor() >= 240:
            return True

    def move_missile(self):
        self.missile.showturtle()

        missile_ycor = self.missile.ycor()
        missile_ycor += 15

        self.missile.sety(missile_ycor)

    def reload_missile(self):
        self.missile.hideturtle()
        self.missile.sety(300)

        self.missile_state = "ready"
