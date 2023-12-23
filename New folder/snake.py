from random import randint

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake_segments = [(100, 100)]  # Initial snake position
        self.food_pos = (0, 0)
        self.direction = 'right'
        self.grid_size = 20
        self.spawn_food()

    def spawn_food(self):
        self.food_pos = (randint(0, self.width - self.grid_size),
                         randint(0, self.height - self.grid_size))

    def update_snake(self):
        head_x, head_y = self.snake_segments[0]
        if self.direction == 'up':
            head_y += self.grid_size
        elif self.direction == 'down':
            head_y -= self.grid_size
        elif self.direction == 'left':
            head_x -= self.grid_size
        elif self.direction == 'right':
            head_x += self.grid_size

        self.snake_segments.insert(0, (head_x, head_y))

        if head_x == self.food_pos[0] and head_y == self.food_pos[1]:
            self.spawn_food()
        else:
            self.snake_segments.pop()

        return head_x, head_y
