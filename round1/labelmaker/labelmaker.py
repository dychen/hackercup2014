FILENAME = 'labelmaker_example_input.txt'
OUTPUT = 'labelmaker_output.txt'

def calc_label(alphabet, target, L):
    N = target
    num_letters = len(alphabet)
    label = ''
    bounds = [0] * L
    bounds[0] = 1
    for i in range(1, L):
        bounds[i] = bounds[i-1] + num_letters ** i
    for j in range(len(bounds)-1, -1, -1):
        bound = bounds[j]
        if N >= bound:
            idx = (N - bound) / (num_letters ** j)
            label += alphabet[idx]
            N -= (idx+1) * (num_letters ** j)
    return label

if __name__ == '__main__':
    f = open(FILENAME)
    f_out = open(OUTPUT, 'w')
    NUM_INPUT = int(f.readline())
    for i in range(NUM_INPUT):
        line = f.readline().split()
        alphabet = list(line[0])
        target = int(line[1])
        label = calc_label(alphabet, target, 25)
        print "Case #" + str(i+1) + ": " + label
        #f_out.write("Case #" + str(i+1) + ": " + label + '\n')
    f.close()
    f_out.close()
