class Laser:

    def __init__(self, turtle) -> None:
        self.turtle = turtle

    def shoot_laser_method(self):
        laser = self.turtle.Turtle()
        laser.hideturtle()

        laser.penup()
        laser.speed(0)

        laser.shape("circle")
        laser.shapesize(0.75)
        laser.color("black")

        laser_xcor = 0
        laser_ycor = 700

        laser.setposition(laser_xcor, laser_ycor)

        return laser

    def move_laser(self, laser):
        laser_ycor = laser.ycor()
        laser_ycor -= 40

        laser.sety(laser_ycor)

    def show_laser(self, laser, boss):
        laser_xcor = boss.xcor()
        laser.setx(laser_xcor)

        laser.showturtle()

    def reset_laser(self, laser):
        laser.hideturtle()
        laser.sety(350)
