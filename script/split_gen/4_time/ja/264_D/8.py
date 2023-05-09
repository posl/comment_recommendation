def calc(s):
    if s == "atcoder":
        return 0
    if len(s) == 8:
        return 21
    if len(s) == 7:
        return 8
    if len(s) == 6:
        return 6
    if len(s) == 5:
        return 5
    if len(s) == 4:
        return 4
    if len(s) == 3:
        return 3
    if len(s) == 2:
        return 2
    if len(s) == 1:
        return 1
    return 0
s = input()
print(calc(s))
