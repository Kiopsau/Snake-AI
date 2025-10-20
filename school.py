import random
from environment import SnakeEnvironment
from idiot import suckers
import config
import time


POPULATION = config.IDIOTS
GENERATIONS = config.GENERATIONS
MUTATION_RATE = config.MUTATION_RATE


def mutate(weights):
    new_weights = [weights[0], weights[1], weights[2], list(weights[3]), list(weights[4]), list(weights[5])]  


    new_weights[3][0] += random.uniform(-config.MUTATION_RATE * weights[4][0], config.MUTATION_RATE * weights[4][0]) #base


    new_weights[3][1] += random.uniform(-config.MUTATION_RATE * weights[4][0], config.MUTATION_RATE * weights[4][0]) #exp


    new_weights[0] += random.uniform(-config.MUTATION_RATE, config.MUTATION_RATE)  # moving
    new_weights[1] += random.uniform(-config.MUTATION_RATE, config.MUTATION_RATE)  # food
    new_weights[2] += random.uniform(-config.MUTATION_RATE, config.MUTATION_RATE)  # death


    new_weights[4][0] += random.uniform(-config.MUTATION_RATE * weights[4][1], config.MUTATION_RATE * weights[4][1])
    new_weights[4][1] += random.uniform(-config.MUTATION_RATE * weights[4][1], config.MUTATION_RATE * weights[4][1])


    new_weights[5][0] += random.uniform(-config.MUTATION_RATE, config.MUTATION_RATE)
    new_weights[5][1] += random.uniform(-config.MUTATION_RATE, config.MUTATION_RATE)


    return new_weights


def evolve(parent):
    agents = [suckers(weights=parent.weights)]
    for _ in range(POPULATION - 1):
        new_weights = mutate(parent.weights)
        agents.append(suckers(weights=new_weights))
    return agents


def run_agent(agent, render=False, num_runs = 1):
    total_score = 0
    total_length = 0
    total_moves = 0


    for _ in range(num_runs):
        env = SnakeEnvironment(render = render)
        state = env.reset()
        done = False
        score = 0
        moves = 0


        while not done:
            action = agent.get_action(state, env)
            state, reward, done = env.step(action)
            score += reward
            moves += 1


            if render:
                env.render()


        total_score += score
        total_moves += moves
        total_length += len(env.snake.body)


    avg_score = total_score / num_runs
    avg_length = total_length / num_runs
    avg_moves = total_moves / num_runs
    return avg_score, avg_length, avg_moves


def main():
    agents = [suckers(weights=config.WEIGHTS) for _ in range(POPULATION)]


    for gen in range(1, GENERATIONS + 1):
        start_time = time.time()
        print(f"\n--- Generation {gen} ---")
        scores = []
        lengths = []
        moves = []
        weighted_scores = []


        for agent in agents:
            score, length, num_moves = run_agent(agent, render=False, num_runs = config.NUM_RUNS)
            scores.append(score)
            lengths.append(length)
            moves.append(num_moves)


            weighted_scores.append((score * agent.weights[5][0]) - (length * agent.weights[5][1]) + (length * agent.weights[5][2]))


        best_idx = weighted_scores.index(max(weighted_scores))
        smartest = agents[best_idx]


        print(f"Best weighted agent score: {weighted_scores[best_idx]:.2f} | length: {lengths[best_idx]:.2f} | moves: {moves[best_idx]:.2f} | Weights: {smartest.weights}")


        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Generation {gen} took {duration: .2f} milliseconds")


        run_agent(smartest, render=True)
        agents = evolve(smartest)


if __name__ == "__main__":
    main()
