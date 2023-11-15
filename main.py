import turtle
import random
import math
import time
import winsound

from modules.Level import Level
from modules.Rules import Rules
from modules.Sounds import Sounds
from modules.Border import Border
from modules.Player import Player
from modules.Missile import Missile
from modules.Invaders import Invaders
from modules.Score import Score
from modules.Boss import Boss
from modules.Laser import Laser
from modules.GameOver import Game_over

window = turtle.Screen()
window.setup(width=600, height=600)
window.title("Space Invaders")

level = Level(window=window)
game_level = level.change_level()

rules = Rules(math=math)

sounds = Sounds(winsound=winsound)
sounds.play_sound("start_game")

border = Border(turtle=turtle)
border.create_border()
border.add_background()

player = Player(turtle=turtle)
new_player = player.create_player()

control_missile = Missile(turtle=turtle, player=new_player, sounds=sounds)
missile = control_missile.create_missile()

shoot_missile = control_missile.shoot_missile

invaders = Invaders(turtle=turtle, random=random, game_level=game_level)
invaders_arr = invaders.create_invader()

score = Score(turtle=turtle)
score_pen = score.start_score()

boss_exists = False
create_boss = Boss(turtle=turtle)


if game_level["level"] == "hard":
    global boss, hp_boss, laser, shoot_laser, shoot_laser_status

    boss = create_boss.create()
    boss_exists = True

    hp_boss = create_boss.hp_boss()

    laser_control = Laser(turtle=turtle)
    laser = laser_control.shoot_laser_method()

    shoot_laser_status = "ready"


window.listen()
window.onkey(shoot_missile, "space")

game_over = Game_over(turtle=turtle, window=window, time=time)

while True:

    if control_missile.check_missile_position(moviment=True) and control_missile.check_missile_status():
        control_missile.move_missile()

    elif control_missile.check_missile_position(reload=True):
        control_missile.reload_missile()

    missile_position = rules.calculate_position(element=missile)
    for invader in invaders_arr:
        invader.forward(game_level["invaders_movement"])

        if invader.xcor() < -240 or invader.xcor() > 240:
            invaders.move_invader(invader=invader)

        invader_position = rules.calculate_position(element=invader)
        if rules.is_collision(first_element=invader_position, second_element=missile_position):
            sounds.play_sound("killed")
            control_missile.reload_missile()

            invader.setposition(-240, 200)
            game_level["invaders_movement"] += 0.25

            score.update_score(score_pen=score_pen)

        player_position = rules.calculate_position(element=new_player)
        if rules.is_collision(first_element=invader_position, second_element=player_position, sensibility=40):
            sounds.play_sound("game_over")

            new_player.hideturtle()
            game_over.lose()

    if boss_exists:
        create_boss.move_boss(boss=boss)
        laser_control.move_laser(laser=laser)

        if laser.ycor() < 240 and shoot_laser_status == "ready":
            laser_control.show_laser(laser=laser, boss=boss)
            shoot_laser_status = "fire"

        if laser.ycor() < -240:
            laser_control.reset_laser(laser=laser)
            shoot_laser_status = "ready"

        boss_position = rules.calculate_position(element=boss)
        if rules.is_collision(first_element=boss_position, second_element=missile_position, sensibility=30):
            boss_exists = create_boss.update_hp(
                boss=boss, hp_boss=hp_boss, laser=laser, sounds=sounds)
            control_missile.reload_missile()

        laser_position = rules.calculate_position(element=laser)
        if rules.is_collision(first_element=laser_position, second_element=player_position, sensibility=20):
            sounds.play_sound("game_over")

            new_player.hideturtle()
            laser.hideturtle()

            game_over.lose()
