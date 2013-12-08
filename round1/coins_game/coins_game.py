#FILENAME = 'coins_game_example_input.txt'
FILENAME = 'coins_game.txt'
OUTPUT = 'coins_game_output.txt'

def calculate(num_jars, num_coins, target):
    record = [0] * N
    # Build the array that contains the minimum number of moves for each number of jars
    # from 1 to N. Note that the array indices are offset by 1 from the number of jars.
    record[0] = target
    for i in range(1, len(record)):
        # Calculate minimal number of moves on an even distribution
        even_dist = max((((target-1) / (i+1) + 1) * (i+1)) - (num_coins - target), target)
        # Even distribution vs at least one empty jar
        record[i] = min(even_dist, record[i-1]+1)
    return record[-1]

if __name__ == '__main__':
    f = open(FILENAME)
    f_out = open(OUTPUT, 'w')
    NUM_INPUT = int(f.readline())
    for i in range(NUM_INPUT):
        N, K, C = map(lambda x: int(x), f.readline().split())
        P = calculate(N, K, C)
        #print "Case #" + str(i+1) + ": " + str(P)
        f_out.write("Case #" + str(i+1) + ": " + str(P) + '\n')
    f.close()
    f_out.close()
