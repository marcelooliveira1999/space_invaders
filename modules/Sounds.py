class Sounds:

    def __init__(self, winsound) -> None:
        self.winsound = winsound

    def play_sound(self, sound):
        if sound == "start_game":
            self.winsound.PlaySound(
                "assets/sounds/start_game.wav", self.winsound.SND_ASYNC)
        elif sound == "shoot":
            self.winsound.PlaySound(
                "assets/sounds/shoot.wav", self.winsound.SND_ASYNC)
        elif sound == "killed":
            self.winsound.PlaySound(
                "assets/sounds/invader_killed.wav", self.winsound.SND_ASYNC)
        elif sound == "game_over":
            self.winsound.PlaySound(
                "assets/sounds/game_over.wav", self.winsound.SND_ASYNC)
        elif sound == "explosion":
            self.winsound.PlaySound(
                "assets/sounds/explosion.wav", self.winsound.SND_ASYNC)
