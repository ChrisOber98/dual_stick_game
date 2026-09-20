import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Dual Stick Game")

        self.running = True

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    my_game = Game()
    my_game.run_game()