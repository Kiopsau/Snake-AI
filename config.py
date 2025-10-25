WINDOW_SIZE = 400
GRID_SIZE = 20
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 1000


#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


#AI
IDIOTS =  400
GENERATIONS = 1000
MUTATION_RATE = 0.15
NUM_RUNS = 25


WEIGHTS = [-0.01, 10, -100, [1.01, 1.05], [0.1, 0.1], [0.2, 0.6, 1.2]]


WEIGHTS_DESC = {
    0: "moving: penalty per move",
    1: "food: reward per food consumed",
    2: "death: penalty on death",
    3: "procedural length reward: [base, exponent] exponential reward for longer snake",
    4: "procedural length reward modifiers: [v1, v2] multiplicative mutation modifer for procedural length reward (v1 affect mutation_rate for procedural length reward values, v2 affects v1 mutation rate)",
    5: "score modifiers: [modifier for base score, modifier for further move penalty, modifier for further length reward] multiplier for base score before any further modification, move penalty linearly multiplies; length reward linearly multiplies"
}
