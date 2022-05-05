players = input().split()
fouls = {}

for player in players:
    # 1. 파울 목록에 이름이 이미 있다
    if player in fouls:
        fouls[player] += 1
    # 2. 파울 목록에 이름이 없다
    else:
        fouls[player] = 1

min_foul = min(fouls.values()) # 2

for player, foul in fouls.items():
    if foul == min_foul:
        print(player)

print(min_foul)
