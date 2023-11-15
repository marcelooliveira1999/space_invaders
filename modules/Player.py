class Player:

    def __init__(self, turtle) -> None:
        self.turtle = turtle

    def create_player(self):
        self.turtle.register_shape("assets/img/ship.gif")

        player = self.turtle.Turtle()
        player.shape("assets/img/ship.gif")
        player.speed(0)

        player.up()
        player.setposition(0, -210)

        def move_player_right():
            movement_x = player.xcor()
            movement_y = player.ycor()

            if movement_x > 220:
                return

            movement_x += 10

            player.setposition(movement_x, movement_y)

        def move_player_left():
            movement_x = player.xcor()
            movement_y = player.ycor()

            if movement_x < -220:
                return

            movement_x -= 10

            player.setposition(movement_x, movement_y)

        self.turtle.listen()

        self.turtle.onkey(move_player_right, "Right")
        self.turtle.onkey(move_player_left, "Left")

        return player
