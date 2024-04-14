"""
Class: ETEST programming class
Flappy Bird Class
Author: 
Date: 

This is the implementation of the main class
for this program, FlappyBird.

"""

import pygame
from pygame.locals import *
import random

from flappy.Bird import Bird
from flappy.Pipe import Pipe
from flappy.constants import FPS, GROUND_Y, MAX_LEVEL, SCORE_PER_LEVEL, SCREEN_HEIGHT, SCREEN_WIDTH

class FlappyBird:
    """
    This class implements the Flappy Bird game

    :return: None
    """

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('Flappy Bird')
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.SysFont('Bauhaus 93', 60)
        self.font_info = pygame.font.SysFont('Bauhaus 93', 30)
        self.text_color_white = (255, 255, 255)
        self.text_color_yellow = (255, 255, 0)

        self.src_img_background_day = pygame.image.load('images/background-day.png')
        self.src_img_background_night = pygame.image.load('images/background-night.png')
        self.src_img_ground = pygame.image.load('images/base.png')

        self.is_program_running = True
        self.is_game_started = False
        self.is_game_over = False
        self.high_score = 0

        self.current_user_score = 0
        self.current_user_level = 1
        self.current_user_scroll_speed = 2

        self.is_pipe_encountered = False
        self.ground_scroll = 0
        self.last_piped_time = pygame.time.get_ticks()

    def run_game(self):
        # objects
        pipe_group = pygame.sprite.Group()      # a list of sprites
        bird_group = pygame.sprite.Group()
        bird = Bird(x=50, y=int(SCREEN_HEIGHT / 2), level=1, current_speed=1)
        bird_group.add(bird)

        while self.is_program_running:
            # For every loop, the clock will tick, which will
            # make the game run
            self.clock.tick(FPS)

            # Set current user level as a function of score
            self.current_user_level = min(MAX_LEVEL, int(self.current_user_score / SCORE_PER_LEVEL) + 1)

            # Set scroll speed = level + 1
            self.current_user_scroll_speed = self.current_user_level + 1

            bird.level = self.current_user_level
            bird.current_speed = self.current_user_scroll_speed

            # Draw background (first, so that every subsequent things can overlap background)
            self.screen.blit(self.src_img_background_night if self.current_user_level >= int(MAX_LEVEL - 2) 
                        else self.src_img_background_day, (0, 0))
            
            # Draw bird
            bird_group.draw(self.screen)

            # Draw pipe
            pipe_group.draw(self.screen)

            # Draw ground (last, since ground must overlap everything else)
            self.screen.blit(self.src_img_ground, (self.ground_scroll, GROUND_Y))

            # Draw title and special texts
            if not self.is_game_over and not self.is_game_started:
                self.screen.blit(pygame.image.load('images/message.png'), (40, SCREEN_HEIGHT / 3))
            elif self.is_game_over:
                self.screen.blit(pygame.image.load('images/gameover.png'), (40, SCREEN_HEIGHT / 3))

            # Update bird per clock tick 
            bird_group.update(is_game_started=self.is_game_started, 
                              is_game_over=self.is_game_over, 
                              level=self.current_user_level,
                              score=self.current_user_score)
            
            # Bonus score if hit top of screen
            if bird_group.sprites()[0].rect.y == 0:
                self.current_user_score += 2

            # Update score
            if len(pipe_group) > 0:
                self.update_score(bird=bird, pipe=pipe_group.sprites()[0])
     
            # Get and draw score and high score
            self.get_and_draw_scores()
       
            # collision logics
            # the Falses are for killing collisions (deleting either or both objects upon 
            # collision)
            self.update_game_over_status(bird_group=bird_group, 
                                         pipe_group=pipe_group)

            # When game starts, render pipes + scroll both pipes and ground
            if not self.is_game_over and self.is_game_started:
                time_now = pygame.time.get_ticks()
                if time_now - self.last_piped_time > 2000 + (2000 if self.current_user_score == SCORE_PER_LEVEL else 0) + random.randint(0, 1000):
                    self.create_pipe_set(pipe_group)
                    self.last_piped_time = time_now
                pipe_group.update(is_game_over=self.is_game_over)
                
                # Scroll ground
                self.ground_scroll -= (self.current_user_scroll_speed - 1 if self.current_user_score == SCORE_PER_LEVEL else self.current_user_scroll_speed)
                if abs(self.ground_scroll) > 46:
                    self.ground_scroll = 0

            for event in pygame.event.get():
                self.handle_quit(event)
                self.handle_start_game(event)
                self.handle_reset_game(event, bird, pipe_group)

            pygame.display.update()

        pygame.quit()

    def create_pipe_set(self, pipe_group):
        """
        Create a set of pipes that includes 1 normal pipe and 1 upside-down 
        pipe, with gap between them = MIN_PIPE_GAP. These pipes with be 
        situated at x=SCREEN_WIDTH and y=SCREEN_HEIGHT / 2 + a random integer 
        between -90 and 90.

        Hard
        """
        rand_int = random.randint(-90, 90)
        ground_pipe = Pipe(x=SCREEN_WIDTH, y=SCREEN_HEIGHT / 2 + rand_int, 
                            level=self.current_user_level, 
                            current_speed=self.current_user_scroll_speed, 
                            orientation=0)
        sky_pipe = Pipe(x=SCREEN_WIDTH, y=SCREEN_HEIGHT / 2 + rand_int, 
                            level=self.current_user_level, 
                            current_speed=self.current_user_scroll_speed, 
                            orientation=1)
        pipe_group.add(ground_pipe)
        pipe_group.add(sky_pipe)
            

    def update_score(self, bird, pipe):
        """ 
        Hard

        """
        bird_left = bird.rect.left
        bird_right = bird.rect.right
        pipe_left = pipe.rect.left
        pipe_right = pipe.rect.right

        if bird_left >= pipe_left \
                and bird_right < pipe_right:
            self.is_pipe_encountered = True

        if bird_left >= pipe_right \
            and self.is_pipe_encountered == True:
            self.current_user_score += 1 
            self.is_pipe_encountered = False

    def update_game_over_status(self, bird_group, pipe_group):
        """
        Game is over when Flappy collides with a 
        pipe or hits the ground 
        
        Easy
        """
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) \
            or bird_group.sprites()[0].rect.bottom >= GROUND_Y:
            self.is_game_over = True

    def handle_add_bonus_score_when_bird_touched_ceiling(self):
        """
        Bonus
        """
        pass

    def handle_quit(self, event):
        """
        Program stops running if QUIT
        event is encountered

        Easy
        """
        # ---------------- Don't edit these lines
        if event.type == pygame.QUIT:
        # ---------------- Don't edit these lines
            self.is_program_running = False


    def handle_start_game(self, event):
        """
        Demo
        """
        if (event.type == pygame.MOUSEBUTTONDOWN 
            or (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP))) \
                and self.is_game_started == False:
            self.is_game_started = True

    def handle_reset_game(self, event, bird, pipe_group):
        """
        Reset game when it is game over and the user right clicked or 
        pressed the Spacebar/Up-arrow key

        The score must be reset, as well as 
        the game_over and game_started statuses

        The bird's position must also be reset,
        and pipe_group must be cleared

        Medium
        """
        if (event.type == pygame.MOUSEBUTTONDOWN 
                or (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP))) \
                and self.is_game_over == True:
            self.current_user_score = 0
            self.is_game_over = False
            self.is_game_started = True

            # ---------------- Don't edit these lines
            bird.reset()
            pipe_group.empty()
            # ---------------- Don't edit these lines
            

    def draw_text(self, text, font, color, x, y):
        """
        N/A
        """
        # ---------------- Don't edit these lines
        img = font.render(text, True, color)
        self.screen.blit(img, (x, y))
        # ---------------- Don't edit these lines

    def get_and_draw_scores(self):
        """
        Medium
        """
        # ---------------- Don't edit these lines
        self.draw_text(f'Score: {str(self.current_user_score)}', self.font_info, self.text_color_white, 10, 20)
        # ---------------- Don't edit these lines

        # Compare high score with max score for every loop
        self.high_score = max(self.current_user_score, self.high_score)
        self.draw_text(f'High score: {str(self.high_score)}', self.font_info, self.text_color_white, 10, 50)

