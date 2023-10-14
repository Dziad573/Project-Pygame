import pygame
import sys


class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)

    def move(self, dx, dy):
        self.position.x += dx
        self.position.y += dy


class Game:
    def __init__(self):
        pygame.init()
        self.res = (1280, 720)
        self.screen = pygame.display.set_mode(self.res)
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        self.max_tps = 90
        self.red = (255, 0, 0)

        self.player_pos = Player(self.screen.get_width() / 2, self.screen.get_height() / 2)

        self.game_over_element_x = 700
        self.game_over_element_y = 300
        self.box = pygame.Rect(self.game_over_element_x, self.game_over_element_y, 100, 50)

        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    #def update(self):

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.render()

if __name__ == "__main__":
    game = Game()
    game.run()