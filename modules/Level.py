class Level:
    game_level = {}

    level_easy = {
        "level": "easy",
        "amount_invaders": 5,
        "invaders_movement": 4,
        "advance_of_the_invaders": 30,
        "missile_speed": 20
    }

    level_normal = {
        "level": "normal",
        "amount_invaders": 7,
        "invaders_movement": 6,
        "advance_of_the_invaders": 35,
        "missile_speed": 25
    }

    level_hard = {
        "level": "hard",
        "amount_invaders": 5,
        "invaders_movement": 8,
        "advance_of_the_invaders": 40,
        "missile_speed": 25
    }

    def __init__(self, window) -> None:
        self.window = window

    def change_level(self):
        self.window.bgpic("assets/img/load-wallpaper.gif")

        user_input = self.window.textinput(
            "Difficulty:", "1 - easy\n2 - normal \n3 - hard\n\n")

        if user_input == "1":
            self.game_level = self.level_easy
        elif user_input == "2":
            self.game_level = self.level_normal
        elif user_input == "3":
            self.game_level = self.level_hard
        else:
            self.game_level = self.level_easy

        self.window.bgpic("assets/img/game-wallpaper.gif")

        return self.game_level
