def getPermutation(s, k):
    # write code here
    if len(s) == 1:
        return s
    if k == 1:
        return ''.join(sorted(s))
    if k == 2:
        return s[1]+s[0]
    if k == 3:
        return s[0]+s[2]+s[1]
    if k == 4:
        return s[1]+s[2]+s[0]
    if k == 5:
        return s[2]+s[0]+s[1]
    if k == 6:
        return s[2]+s[1]+s[0]
    if k == 7:
        return s[0]+s[1]+s[2]
    if k == 8:
        return s[0]+s[2]+s[1]
    if k == 9:
        return s[1]+s[0]+s[2]
    if k == 10:
        return s[1]+s[2]+s[0]
    if k == 11:
        return s[2]+s[1]+s[0]
    if k == 12:
        return s[2]+s[0]+s[1]
    if k == 13:
        return s[0]+s[1]+s[2]
    if k == 14:
        return s[0]+s[2]+s[1]
    if k == 15:
        return s[1]+s[0]+s[2]
    if k == 16:
        return s[1]+s[2]+s[0]
    if k == 17:
        return s[2]+s[1]+s[0]
    if k == 18:
        return s[2]+s[0]+s[1]
    if k == 19:
        return s[0]+s[1]+s[2]
    if k == 20:
        return s[0]+s[2]+s[1]
    if k == 21:
        return s[1]+s[0]+s[2]
    if k == 22:
        return s[1]+s[2]+s[0]
    if k == 23:
        return s[2]+s[1]+s[0]
    if

if __name__ == '__main__':
    getPermutation()