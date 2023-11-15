class Score:
    current_score = 0

    def __init__(self, turtle) -> None:
        self.turtle = turtle

    def start_score(self):
        score_pen = self.turtle.Turtle()

        score_pen.speed(0)
        score_pen.color(1, 1, 1)

        score_pen.penup()
        score_pen.setposition(-290, 280)

        score_str = f"SCORE: {self.current_score}"
        score_pen.write(score_str)
        score_pen.hideturtle()

        return score_pen

    def update_score(self, score_pen):
        score_pen.clear()
        self.current_score += 10

        score_str = f"SCORE: {self.current_score}"
        score_pen.write(score_str)
        score_pen.hideturtle()
