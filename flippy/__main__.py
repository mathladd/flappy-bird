"""
Class: ETEST beginner programming class
Flippy Bird
Author: 
Date: 

"""

from pygame.locals import *

from flippy.core import FlappyBird
from flippy.constants import *
from colorama import Fore

class Flippy(FlappyBird):
    pass

if __name__ == '__main__':
    flippy = Flippy()

    # flippy.make_ground('images/base.png')
    # flippy.make_background(
    #     {
    #         1: 'images/background-day.png',
    #         2: 'images/background-day.png',
    #         3: 'images/background-day.png',
    #         4: 'images/background-night.png',
    #     }
    # )

    # bird_level_dictionary = {}
    # for level in range(10):
    #     if level < 3:
    #         bird_level_dictionary[level] = ['images/bluebird-downflap.png', 'images/bluebird-midflap.png', 'images/bluebird-upflap.png']
    #     elif level < 6:
    #         bird_level_dictionary[level] = ['images/redbird-downflap.png', 'images/redbird-midflap.png', 'images/redbird-upflap.png']
    #     else:
    #         bird_level_dictionary[level] = ['images/yellowbird-downflap.png', 'images/yellowbird-midflap.png', 'images/yellowbird-upflap.png']
    # flippy.create_bird(bird_level_dictionary)

    # flippy.make_pipes(
    #     {
    #         1:'images/pipe-green.png'
    #     }
    # )

    # flippy.make_score()

    # flippy.make_intro('images/message.png')

    # flippy.show_gameover('images/gameover.png')

    print(Fore.GREEN + 'Flappy bird is now running!')
    flippy.run_game()
