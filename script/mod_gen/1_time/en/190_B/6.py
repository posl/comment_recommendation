def canDoDamage(N, S, D, spells):
    for spell in spells:
        if spell[0] < S or spell[1] > D:
            return "Yes"
    return "No"

if __name__ == '__main__':
    canDoDamage()