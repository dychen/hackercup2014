from collections import deque

FILENAME = 'aaaaaa_example_input.txt'
FILENAME = 'aaaaaa1.txt'
OUTPUT = 'aaaaaa_output.txt'

def longest_path(mat):
    rows = len(mat)
    cols = len(mat[0])
    mat2 = [row[:] for row in mat]
    mat3 = [row[:] for row in mat]
    mat[0][0] = 1
    q = deque([(0, 0, -1, 0)])
    # Down/right
    num_iter = 0
    while len(q) > 0:
        # prevdir (previous block was in what direction) - 0: up, 1: left, 2: down, 3: right
        # state - 0: first down/right iteration, 1: up/left, 2: second down/right iteration
        r, c, prevdir, state = q.popleft()
        if state == 0:
            # Move down
            if r+1 < rows and mat[r+1][c] >= 0:
                if (mat[r][c] + 1 > mat[r+1][c]):
                    mat[r+1][c] = mat[r][c] + 1
                    q.append((r+1, c, 0, 0))
            # Move right
            if c+1 < cols and mat[r][c+1] >= 0:
                if (mat[r][c] + 1 > mat[r][c+1]):
                    mat[r][c+1] = mat[r][c] + 1
                    q.append((r, c+1, 1, 0))
            # Move up -> State transition
            if r-1 >= 0 and mat[r-1][c] >= 0 and prevdir != 0:
                mat2[r-1][c] = max(mat[r-1][c], mat[r][c] + 1)
                q.append((r-1, c, 2, 1))
            # Move left -> State transition
            if c-1 >= 0 and mat[r][c-1] >= 0 and prevdir != 1:
                mat2[r][c-1] = max(mat[r][c-1], mat[r][c] + 1)
                q.append((r, c-1, 3, 1))
        elif state == 1:
            # Move up
            if r-1 >= 0 and mat2[r-1][c] >= 0 and prevdir == 2:
                mat2[r-1][c] = max(mat2[r-1][c], mat2[r][c] + 1)
                q.append((r-1, c, 2, 1))
            # Move left
            if c-1 >= 0 and mat2[r][c-1] >= 0 and prevdir == 3:
                mat2[r][c-1] = max(mat2[r][c-1], mat2[r][c] + 1)
                q.append((r, c-1, 3, 1))
            # Move down -> State transition
            if r+1 < rows and mat2[r+1][c] >= 0 and prevdir != 2:
                mat3[r+1][c] = max(mat2[r+1][c], mat2[r][c] + 1)
                q.append((r+1, c, 0, 2))
            # Move right -> State transition
            if c+1 < cols and mat2[r][c+1] >= 0 and prevdir != 3:
                mat3[r][c+1] = max(mat2[r][c+1], mat2[r][c] + 1)
                q.append((r, c+1, 1, 2))
        elif state == 2:
            # Move down
            if r+1 < rows and mat3[r+1][c] >= 0 and prevdir != 2:
                if (mat3[r][c] + 1 > mat3[r+1][c]):
                    mat3[r+1][c] = max(mat3[r+1][c], mat3[r][c] + 1)
                    q.append((r+1, c, 0, 2))
            # Move right
            if c+1 < cols and mat3[r][c+1] >= 0 and prevdir != 3:
                if (mat3[r][c] + 1 > mat3[r][c+1]):
                    mat3[r][c+1] = max(mat3[r][c+1], mat3[r][c] + 1)
                    q.append((r, c+1, 1, 2))
        num_iter += 1
    print "NUM ITER: " + str(num_iter)
    max_len = -1
    for row in mat:
        max_len = max(max_len, max(row))
    for row in mat2:
        max_len = max(max_len, max(row))
    for row in mat3:
        max_len = max(max_len, max(row))
    '''
    print "======="
    print "MATRIX1"
    for p_row in mat:
        print p_row
    print "MATRIX2"
    for p_row in mat2:
        print p_row
    print "MATRIX3"
    for p_row in mat3:
        print p_row
    '''
    return max_len


if __name__ == '__main__':
    f = open(FILENAME)
    f_out = open(OUTPUT, 'w')
    NUM_INPUT = int(f.readline())
    for i in range(NUM_INPUT):
        rows, cols = map(lambda x: int(x), f.readline().split())
        mat = [[0 for c in range(cols)] for r in range(rows)]
        print "==CASE=="
        print rows, cols
        for row in range(rows):
            car_indices = [idx for idx, char in enumerate(f.readline()) if char == '#']
            for car_index in car_indices:
                mat[row][car_index] = -1
        longest = longest_path(mat)
        print "Case #" + str(i+1) + ": " + str(longest)
        #f_out.write("Case #" + str(i+1) + ": " + str(longest) + "\n")
    f.close()
    f_out.close()