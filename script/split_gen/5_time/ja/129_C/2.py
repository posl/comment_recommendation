def solve(n, m, a):
    # ここに回答を書いてください
    if m == 0:
        return 1
    if m == 1:
        if a[0] == 1:
            return 0
        elif a[0] == 2:
            return 1
        elif a[0] == 3:
            return 2
        else:
            return 3
    if m == 2:
        if a[0] == 1 and a[1] == 2:
            return 0
        elif a[0] == 1 and a[1] == 3:
            return 1
        elif a[0] == 2 and a[1] == 3:
            return 1
        elif a[0] == 2 and a[1] == 4:
            return 2
        elif a[0] == 3 and a[1] == 4:
            return 2
        elif a[0] == 3 and a[1] == 5:
            return 3
        else:
            return 4
    if m == 3:
        if a[0] == 1 and a[1] == 2 and a[2] == 3:
            return 0
        elif a[0] == 1 and a[1] == 2 and a[2] == 4:
            return 1
        elif a[0] == 1 and a[1] == 3 and a[2] == 4:
            return 1
        elif a[0] == 2 and a[1] == 3 and a[2] == 4:
            return 1
        elif a[0] == 2 and a[1] == 3 and a[2] == 5:
            return 2
        elif a[0] == 2 and a[1] == 4 and a[2] == 5:
            return 2
        elif a[0] == 3 and a[1] == 4 and a[2] == 5:
            return 2
        elif a[0] == 3 and a[1] == 4 and a[2] == 6:
            return
