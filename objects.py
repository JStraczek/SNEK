import pygame
import random


class GameObject:

    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y

        self.width = 10
        self.height = 10

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, (0, 0, 0), [self.x_pos, self.y_pos, self.width, self.height])


class Player(GameObject):

    SPEED = 1

    def __init__(self, x, y):
        super().__init__(x, y)
        self.body = []
        self.body.append(Segment(self.x_pos - 10, self.y_pos, self.x_pos, self.y_pos))
        self.body.append(Segment(self.x_pos - 20, self.y_pos, self.x_pos - 10, self.y_pos))
        self.tail = self.body[-1]

    def grow(self):
        self.body.append(Segment(self.tail.x_pos, self.tail.y_pos, self.tail.x_pos, self.tail.y_pos))

    def draw_snek(self, surface):
        self.draw(surface)
        for el in self.body:
            el.draw(surface)

    def check_for_food(self, food):
        if self.x_pos == food.x_pos and self.y_pos == food.y_pos:
            self.grow()
            return True

        return False

    def move(self, x_dir, y_dir):
        if x_dir > 0:
            self.x_pos += self.SPEED*10
        elif x_dir < 0:
            self.x_pos -= self.SPEED*10
        elif y_dir > 0:
            self.y_pos -= self.SPEED*10
        elif y_dir < 0:
            self.y_pos += self.SPEED*10

        new_coords = (self.x_pos, self.y_pos)
        for el in self.body:
            el.move(new_coords)
            new_coords = (el.x_pos, el.y_pos)

    def is_eating_himself(self):
        for segment in self.body:
            if self.x_pos == segment.x_pos and self.y_pos == segment.y_pos:
                return True
        return False

    def is_out_of_bounds(self, resolution):
        if self.x_pos < 0:
            return True
        elif self.x_pos > resolution[0] - 10:
            return True

        if self.y_pos < 0:
            return True
        elif self.y_pos > resolution[1] - 10:
            return True

        return False


class Segment(GameObject):

    def __init__(self, x, y, next_x, next_y):
        super().__init__(x, y)
        self.next_x = next_x
        self.next_y = next_y

    def move(self, new_coords):
        self.x_pos = self.next_x
        self.y_pos = self.next_y

        self.next_x = new_coords[0]
        self.next_y = new_coords[1]


class Food(GameObject):

    def randomize(self):
        self.x_pos = random.randrange(30, 650, 10)
        self.y_pos = random.randrange(30, 450, 10)