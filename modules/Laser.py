class Laser:

    def __init__(self, turtle) -> None:
        self.turtle = turtle

    def shoot_laser_method(self, color, shapesize):
        laser = self.turtle.Turtle()
        laser.hideturtle()

        laser.penup()
        laser.speed(0)

        laser.shape("circle")
        laser.shapesize(shapesize)
        laser.color(color)

        laser_xcor = 0
        laser_ycor = 700

        laser.setposition(laser_xcor, laser_ycor)

        return laser

    def move_laser(self, laser, speed):
        laser_ycor = laser.ycor()
        laser_ycor -= speed

        laser.sety(laser_ycor)

    def show_laser(self, laser, boss):
        laser_xcor = boss.xcor()
        laser.setx(laser_xcor)

        laser.showturtle()

    def reset_laser(self, laser):
        laser.hideturtle()
        laser.sety(350)

    def setposition_laser_invaders(self,laser, invaders_arr, random):
        invader = random.choice(invaders_arr)
        
        laser_xcor = invader.xcor()
        laser_ycor = invader.ycor()
        laser_ycor -= 20

        laser.setposition(laser_xcor,laser_ycor)
        laser.showturtle()