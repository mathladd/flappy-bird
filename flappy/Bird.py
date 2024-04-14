import pygame

from flappy.constants import ALL_BIRD_COLORS, ALL_FLAP_VARIANTS, GROUND_Y, MAX_GRAVITY, MAX_LEVEL, SCREEN_HEIGHT


ALLOWED_KEYS = [pygame.K_SPACE, pygame.K_UP]

class Bird(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, level: int, current_speed: int):
        pygame.sprite.Sprite.__init__(self)
        
        # Start your code here
        self.level = level
        self.current_speed = current_speed
        self.velocity = 0

        self.flap_variant_index = 0
        self.flapping_cooldown_counter = 0
        self.clicked = False
        self.color = ALL_BIRD_COLORS[0]

        img = pygame.image.load(f'images/bluebird-midflap.png')
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    def update(self, is_game_started: bool, is_game_over: bool, level: int, score: int):
        if is_game_over:
            self.image = pygame.transform.rotate(self.all_flap_variants[self.flap_variant_index], -90)    # add rotation
        else:
            # set animation
            self.update_bird_flapping_animation()

        # update color
        self.update_bird_color_by_level(level=level)

        # update fall velocity (only when game started i.e. is_game_started == True)
        if is_game_started:
            # bouncing at the top
            if self.rect.y == 0:
                self.velocity += 50
            else:
                self.velocity = min(MAX_GRAVITY, self.velocity + 0.5)
            if self.rect.bottom < GROUND_Y:
                self.rect.y = max(0, self.rect.y + int(self.velocity))
        
        # handle click jump
        if (pygame.mouse.get_pressed()[0] == 1 or any(pygame.key.get_pressed()[item] for item in ALLOWED_KEYS)) and self.clicked == False:
            self.clicked = True
            self.velocity = -9

        if pygame.mouse.get_pressed()[0] == 0 and not any(pygame.key.get_pressed()[item] for item in ALLOWED_KEYS):
            self.clicked = False

    def update_bird_color_by_level(self, level):
        self.color = ALL_BIRD_COLORS[0] if level < MAX_LEVEL / 2 \
            else ALL_BIRD_COLORS[1] if level < MAX_LEVEL - 1 \
                else ALL_BIRD_COLORS[2]
        
    def update_bird_flapping_animation(self):
        self.all_flap_variants = []
        for num in range(0, len(ALL_FLAP_VARIANTS)):
            flap = ALL_FLAP_VARIANTS[num]
            img = pygame.image.load(f'images/{self.color}bird-{flap}flap.png')
            self.all_flap_variants.append(img)

        self.flapping_cooldown_counter += 1
        flap_cooldown = MAX_LEVEL - self.current_speed
        if self.flapping_cooldown_counter > flap_cooldown:
            self.flapping_cooldown_counter = 0
            self.flap_variant_index += 1
            if self.flap_variant_index > len(ALL_FLAP_VARIANTS) - 1:
                self.flap_variant_index = 0
        self.image = self.all_flap_variants[self.flap_variant_index]
        self.image = pygame.transform.rotate(self.image, self.velocity * -4)    # add rotation

    def reset(self):
        self.rect.x = 50
        self.rect.y = int(SCREEN_HEIGHT / 2)