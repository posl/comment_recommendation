def check(a, s):
    if a > s:
        return False
    if a == 0:
        return s == 0
    if a == s:
        return True
    if a == 1:
        return False
    if a == 2:
        return s == 2
    if a == 3:
        return s == 2 or s == 3
    if a == 4:
        return s == 4
    if a == 5:
        return s == 4 or s == 5
    if a == 6:
        return s == 4 or s == 5 or s == 6
    if a == 7:
        return s == 4 or s == 5 or s == 6 or s == 7
    if a == 8:
        return s == 8
    if a == 9:
        return s == 8 or s == 9
    if a == 10:
        return s == 8 or s == 9 or s == 10
    if a == 11:
        return s == 8 or s == 9 or s == 10 or s == 11
    if a == 12:
        return s == 12
    if a == 13:
        return s == 12 or s == 13
    if a == 14:
        return s == 12 or s == 13 or s == 14
    if a == 15:
        return s == 12 or s == 13 or s == 14 or s == 15
    if a == 16:
        return s == 16
    if a == 17:
        return s == 16 or s == 17
    if a == 18:
        return s == 16 or s == 17 or s == 18
    if a == 19:
        return s == 16 or s == 17 or s == 18 or s == 19
    if a == 20:
        return s == 20
    if a == 21:
        return s == 20 or s == 21
    if a == 22:
        return s == 20 or s == 21 or s == 22
    if a == 23:
        return s == 20 or s ==

if __name__ == '__main__':
    check()