"""
Class: ETEST beginner programming class
Flippy Bird
Author: 
Date: 

"""

from pygame.locals import *

from flippy.core import FlappyBird
from flippy.constants import *

class Flippy(FlappyBird):
    pass

if __name__ == '__main__':
    flippy = Flippy()
    flippy.make_ground('images/base.png')
    flippy.make_background(
        {
            1: 'images/background-day.png',
            2: 'images/background-day.png',
            3: 'images/background-day.png',
            4: 'images/background-night.png',
        }
    )
    flippy.create_bird(
        {
            1: ['images/bluebird-downflap.png', 'images/bluebird-midflap.png', 'images/bluebird-upflap.png'],
            2: ['images/redbird-downflap.png', 'images/redbird-midflap.png', 'images/redbird-upflap.png'],
            3: ['images/yellowbird-downflap.png', 'images/yellowbird-midflap.png', 'images/yellowbird-upflap.png'],
        }
    )
    # flippy.make_pipes(
    #     {
    #         1:'images/pipe-green.png'
    #     }
    # )
    # flippy.make_score()
    # flippy.make_intro('images/message.png')
    # flippy.show_gameover('images/gameover.png')
    flippy.run_game()
