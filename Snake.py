import random
import config


class Snake:
    def __init__(self):
        self.body = [(config.GRID_SIZE // 2, config.GRID_SIZE // 2)]
        self.direction = (0, -1)
        self.grow = False


    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False


    def change_direction(self, new_dir):
        dx, dy = new_dir
        cur_dx, cur_dy = self.direction
        if (dx, dy) != (-cur_dx, -cur_dy):
            self.direction = (dx, dy)


    def check_collision(self):
        head = self.body[0]
        if not (0 <= head[0] < config.GRID_SIZE and 0 <= head[1] < config.GRID_SIZE):
            return True
        if head in self.body[1:]:
            return True
        return False


    def set_dir(self, action):
        dx, dy = self.direction
        dir_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        idx = dir_list.index((dx, dy))
        if action == 0:
            new_idx = idx
        elif action == 1:
            new_idx = (idx + 1) % 4
        else:
            new_idx = (idx - 1) % 4
        self.direction = dir_list[new_idx]


#FOOOOOOOOD YUMMMMMYYY


def random_food(snake_body):
    while True:
        pos = (random.randint(0, config.GRID_SIZE - 1), random.randint(0, config.GRID_SIZE - 1))
        if pos not in snake_body:
            return pos