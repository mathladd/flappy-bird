"""
Class: ETEST programming class
Flappy Bird Main File
Author: 
Date: 

This is the entry point for Flappy 
Bird to recreate the classic, 
world-dominating game Flappy the Bird
"""


from flappy.flappy_bird_game import FlappyBird


if __name__ == '__main__':    
    flappyBird = FlappyBird()
    flappyBird.run_game()
