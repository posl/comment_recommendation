def getMinNumOfSpell(N, x, y):
    spells = []
    for i in range(N):
        for j in range(N):
            if i != j:
                spells.append((x[j] - x[i], y[j] - y[i]))
    spells = list(set(spells))
    return len(spells)

if __name__ == '__main__':
    getMinNumOfSpell()