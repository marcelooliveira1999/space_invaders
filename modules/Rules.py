class Rules:

    def __init__(self, math) -> None:
        self.math = math

    def calculate_position(self, element):
        position = [self.math.ceil(element.xcor()),
                    self.math.ceil(element.ycor())]

        return position

    def is_collision(self, first_element, second_element, sensibility=15):
        distance = self.math.sqrt(self.math.pow(first_element[0] - second_element[0], 2)+self.math.pow(
            first_element[1] - second_element[1], 2))

        if distance < sensibility:
            return True
        else:
            return False
