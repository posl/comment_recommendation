def isLightUp(switch, bulb, p):
    for i in range(len(bulb)):
        if p[i] != sum([switch[j-1] for j in bulb[i]]) % 2:
            return False
    return True

if __name__ == '__main__':
    isLightUp()