def mergeSlime(slime):
    #merge
    i = 0
    while i < len(slime) - 1:
        if slime[i] == slime[i + 1]:
            slime[i] = slime[i] + slime[i + 1]
            slime.pop(i + 1)
        else:
            i += 1
    #print(slime)
    #merge again
    i = 0
    while i < len(slime) - 1:
        if slime[i][-1] == slime[i + 1][0]:
            slime[i] = slime[i] + slime[i + 1]
            slime.pop(i + 1)
        else:
            i += 1
    #print(slime)
    return slime

if __name__ == '__main__':
    mergeSlime()