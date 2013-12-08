FILENAME = 'tennison_example_input.txt'

def play_round(p_s, p_r, p_i, p_u, p_w, p_d, p_l):
    '''
    p_won_round = p_i * p_s + (1-p_i) * p_r
    '''
    '''
    p_sun_next = p_i * p_s * p_w * (p_i+p_u) + \
                 p_i * p_s * (1-p_w) * p_i + \
                 p_i * (1-p_s) * p_i + \
                 (1-p_i) * p_r * p_i + \
                 (1-p_i) * (1-p_r) * (1-p_l) * p_i + \
                 (1-p_i) * (1-p_r) * p_l * (p_i-p_d)
    p_rain_next = p_i * p_s * p_w * (1-(p_i+p_u)) + \
                  p_i * p_s * (1-p_w) * (1-p_i) + \
                  p_i * (1-p_s) * (1-p_i) + \
                  (1-p_i) * p_r * (1-p_i) + \
                  (1-p_i) * (1-p_r) * (1-p_l) * (1-p_i) + \
                  (1-p_i) * (1-p_r) * p_l * (1-(p_i-p_d))
    print p_sun_next, p_rain_next
    '''
    probabilities = []
    p_sun_next = []
    # Case 1: Win round, P(sun) increases
    probabilities.append(p_i * p_s * p_w)
    p_sun_next.append(min(p_i + p_u, 1.0))
    # Case 2: Win round, P(sun) stays the same
    probabilities.append(p_i * p_s * (1-p_w) + (1-p_i) * p_r)
    p_sun_next.append(p_i)
    # Case 3: Lose round, P(sun) decreases
    probabilities.append((1-p_i) * (1-p_r) * p_l)
    p_sun_next.append(max(p_i - p_u, 0.0))
    # Case 4: Lose round, P(sun) stays the same
    probabilities.append((1-p_i) * (1-p_r) * (1-p_l) + p_i * (1-p_s))
    p_sun_next.append(p_i)
    return probabilities, p_sun_next

def play_match(wins_left, losses_left, p_s, p_r, p_i, p_u, p_w, p_d, p_l):
    if wins_left == 0:
        return 1
    elif losses_left == 0:
        return 0
    else:
        p_win_match = 0
        probabilities, p_sun_next = play_round(p_s, p_r, p_i, p_u, p_w, p_d, p_l)
        for i in range(len(probabilities)):
            # If he won the round
            if i in [0, 1]:
                p_win_match += probabilities[i] * \
                               play_match(wins_left-1, losses_left, p_s, p_r,
                                          p_sun_next[i], p_u, p_w, p_d, p_l)
            else:
                p_win_match += probabilities[i] * \
                               play_match(wins_left, losses_left-1, p_s, p_r,
                                          p_sun_next[i], p_u, p_w, p_d, p_l)
        return p_win_match

if __name__ == '__main__':
    f = open(FILENAME)
    N = int(f.readline())
    for i in range(N):
        K, p_s, p_r, p_i, p_u, p_w, p_d, p_l = map(lambda x: float(x), f.readline().split())
        if K > 8:
            K = 8
        p_win = play_match(K, K, p_s, p_r, p_i, p_u, p_w, p_d, p_l)
        print p_win
    f.close()

