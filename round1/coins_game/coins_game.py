import sys

FILENAME = 'coins_game_example_input.txt'
FILENAME = 'coins_game1.txt'
OUTPUT = 'coins_games_output.txt'

# Will need to recurse at most 1000000 (max number of jars) times
sys.setrecursionlimit(1000000)

def calculate(num_jars, num_coins, target):
    if num_jars == 1:
        return target
    # Calculate minimal number of moves on an even distribution
    min_moves = max((((target-1) / num_jars + 1) * num_jars) - (num_coins - target), target)
    # Recursively calculate actual minimal number of moves on:
    # Even distribution vs minimal number of moves on N-1 jars
    min_moves = min(min_moves, calculate(num_jars-1, num_coins, target) + 1)
    return min_moves

if __name__ == '__main__':
    f = open(FILENAME)
    f_out = open(OUTPUT, 'w')
    NUM_INPUT = int(f.readline())
    for i in range(NUM_INPUT):
        N, K, C = map(lambda x: int(x), f.readline().split())
        P = calculate(N, K, C)
        print "Case #" + str(i+1) + ": " + str(P)
        #f_out.write("Case #" + str(i+1) + ": " + str(P) + '\n')
    f.close()
    f_out.close()
