#FILENAME = 'square_detector_example_input.txt'
FILENAME = 'square_detector.txt'
OUTPUT = 'square_detector_output.txt'
f = open(FILENAME)
f_out = open(OUTPUT, 'w')
N = int(f.readline().strip())
for i in range(N):
    dim = int(f.readline().strip())
    rect = []
    first_r = -1
    first_c = -1
    last_r = -1
    last_c = -1
    is_filled_square = True
    # Initialize
    for j in range(dim):
        line = f.readline().strip()
        for index, char in enumerate(line):
            if char == '#':
                last_r = j
                last_c = index
                if first_r == -1 and first_c == -1:
                    first_r = j
                    first_c = index
        rect.append(list(line))
    # Check if it's a (potential) square
    if last_r - first_r != last_c - first_c:
        is_filled_square = False
    # Check if it's filled
    for r in range(len(rect)):
        for c in range(len(rect[r])):
            if is_filled_square == False:
                break
            # If it's in the rectangle
            if r >= first_r and r <= last_r and c >= first_c and c <= last_c:
                if rect[r][c] == '.':
                    is_filled_square = False
                    break
            # If it's outside the rectangle
            else:
                if rect[r][c] == '#':
                    is_filled_square = False
                    break
    if is_filled_square:
        f_out.write("Case #" + str(i+1) + ": YES\n")
    else:
        f_out.write("Case #" + str(i+1) + ": NO\n")
f.close()
f_out.close()
