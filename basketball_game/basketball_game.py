from operator import itemgetter

#FILENAME = 'basketball_game_example_input.txt'
FILENAME = 'basketball_game.txt'
OUTPUT = 'basketball_game_output.txt'

def create_teams(players):
    players = sorted(players, key=itemgetter(1, 2), reverse=True)
    team_1 = [x[0] for i, x in enumerate(players) if (i+1) % 2 == 1]
    team_2 = [x[0] for i, x in enumerate(players) if (i+1) % 2 == 0]
    return team_1, team_2

# Note that the current players on the floor repeat every P minutes.
# The permutation for people on the floor at time t is given by:
# For minute 1: [P, P-1, ..., 1]
# For minute 2: [P-1, P-2, ..., P+1]
# For minute P: [1, P+1, ..., 2P-1]
# For minute K: [N-P+1, N-P+2, ..., N], K is the number of team players
# The solution will be the permutation at the following time step (t+1)
def simulate_game(team_1, team_2, M, P):
    team_1_order = team_1[P-1::-1] + team_1[P:] + team_1[P-1::-1]
    team_2_order = team_2[P-1::-1] + team_2[P:] + team_2[P-1::-1]
    team_1_players = team_1_order[M%len(team_1):M%len(team_1)+P]
    team_2_players = team_2_order[M%len(team_2):M%len(team_2)+P]
    team_1_players.extend(team_2_players)
    return sorted(team_1_players)

# Each player is a list where:
# player[0] := name of player
# player[1] := shot percentage
# player[2] := height
if __name__ == '__main__':
    f = open(FILENAME)
    f_out = open(OUTPUT, 'w')
    NUM_INPUT = int(f.readline())
    for i in range(NUM_INPUT):
        N, M, P = map(lambda x: int(x), f.readline().split())
        players = []
        for _ in range(N):
            player = f.readline().split()
            player[1] = int(player[1])
            player[2] = int(player[2])
            players.append(player)
        team_1, team_2 = create_teams(players)
        current_players = simulate_game(team_1, team_2, M, P)
        f_out.write("Case #" + str(i+1) + ": " + ' '.join(current_players) + '\n')
    f.close()
    f_out.close()
