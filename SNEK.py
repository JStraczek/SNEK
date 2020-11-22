from objects import GameObject, Player, Food
import pygame

pygame.init()

SCREEN_TITLE = 'SNEK'
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
resolution = (SCREEN_WIDTH, SCREEN_HEIGHT)
GRAY_COLOR = (192, 192, 192) #RGB
BLACK_COLOR = (20, 20, 20)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 100)


class Game:

    TICK_RATE = 15

    def __init__(self, title, res):
        self.title = title
        self.resolution = res

        self.game_screen = pygame.display.set_mode(res)
        self.game_screen.fill(GRAY_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False

        x_dir = 1
        y_dir = 0

        snek = Player(100, 230)
        food = Food(400, 230)

        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if y_dir != -1:
                            x_dir = 0
                            y_dir = 1
                    elif event.key == pygame.K_DOWN:
                        if y_dir != 1:
                            x_dir = 0
                            y_dir = -1
                    elif event.key == pygame.K_RIGHT:
                        if x_dir != -1:
                            x_dir = 1
                            y_dir = 0
                    elif event.key == pygame.K_LEFT:
                        if x_dir != 1:
                            x_dir = -1
                            y_dir = 0
                elif event.type == pygame.KEYUP:
                    pass

            self.game_screen.fill(GRAY_COLOR)

            snek.draw_snek(self.game_screen)
            snek.move(x_dir, y_dir)
            food.draw(self.game_screen)

            if snek.is_out_of_bounds(self.resolution):
                is_game_over = True
                pygame.display.update()
                clock.tick(self.TICK_RATE)

            if snek.is_eating_himself():
                is_game_over = True
                pygame.display.update()
                clock.tick(self.TICK_RATE)

            if snek.check_for_food(food):
                food.randomize()
                #self.TICK_RATE += 1

            pygame.display.update()
            clock.tick(self.TICK_RATE)


new_game = Game('SNEK', resolution)
new_game.run_game_loop()