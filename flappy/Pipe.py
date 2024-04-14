import pygame

from flappy.constants import MAX_LEVEL, MIN_PIPE_GAP


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, level: int, current_speed: int, orientation: int):
        pygame.sprite.Sprite.__init__(self)
        self.level = level
        self.current_speed = current_speed
        self.orientation = orientation # 1 if pipe is upside-down, 0 if it is not

        # Start your code here
        self.image = pygame.image.load(f'images/pipe-{'green' if self.level < int(MAX_LEVEL / 2) else 'red'}.png')
        self.rect = self.image.get_rect()
        if orientation == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(MIN_PIPE_GAP / 2)]
        if orientation == 0:
            self.rect.topleft = [x, y + int(MIN_PIPE_GAP / 2)]
        
    def update(self, is_game_over: bool):
        if not is_game_over:
            self.rect.x -= self.current_speed
        if self.rect.right < 0:
            self.kill()