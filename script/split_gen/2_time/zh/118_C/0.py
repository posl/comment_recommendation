def min_health(monster):
    monster.sort()
    for i in range(len(monster)-1):
        if monster[i+1] % monster[i] == 0:
            monster[i+1] = monster[i]
    return monster[-1]
