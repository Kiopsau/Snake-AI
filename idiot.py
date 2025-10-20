import config


class suckers:
    def __init__(self, weights):
        self.weights = weights


    def get_action(self, state, env):
        hx, hy, fx, fy, dx, dy = state
        directions = self.get_possible_directions((dx, dy))
        best_score = float('-inf')
        best_action = 0


        for action, (ndx, ndy) in enumerate(directions):
            nx, ny = hx + ndx, hy + ndy
            if (nx, ny) in env.snake.body or not (0 <= nx < config.GRID_SIZE) or not (0 <= ny < config.GRID_SIZE):
                continue
            score = self.weights[0]
            if abs(nx - fx) + abs(ny - fy) < abs(hx - fx) + abs(hy - fy):
                score += self.weights[1]
            if score > best_score:
                best_score = score
                best_action = action
        return best_action


    def get_possible_directions(self, current_direction):
        dx, dy = current_direction
        dir_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        idx = dir_list.index((dx, dy))
        straight = dir_list[idx]
        right = dir_list[(idx + 1) % 4]
        left = dir_list[(idx - 1) % 4]
        return [straight, right, left]