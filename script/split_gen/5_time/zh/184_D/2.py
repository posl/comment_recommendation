def solve(A,B,C):
    # 1. 三种硬币都有的时候
    if A > 0 and B > 0 and C > 0:
        return 1 + A / (A + B + C) * solve(A + 1, B - 1, C) + B / (A + B + C) * solve(A, B + 1, C - 1) + C / (A + B + C) * solve(A - 1, B, C + 1)
    # 2. 只有两种硬币的时候
    elif A == 0 and B > 0 and C > 0:
        return 1 + B / (B + C) * solve(0, B + 1, C - 1) + C / (B + C) * solve(0, B - 1, C + 1)
    elif A > 0 and B == 0 and C > 0:
        return 1 + A / (A + C) * solve(A + 1, 0, C - 1) + C / (A + C) * solve(A - 1, 0, C + 1)
    elif A > 0 and B > 0 and C == 0:
        return 1 + A / (A + B) * solve(A + 1, B - 1, 0) + B / (A + B) * solve(A - 1, B + 1, 0)
    # 3. 只有一种硬币的时候
    elif A == 0 and B == 0 and C > 0:
        return 1 + solve(0, 0, C + 1)
    elif A == 0 and B > 0 and C == 0:
        return 1 + solve(0, B + 1, 0)
    elif A > 0 and B == 0 and C == 0:
        return 1 + solve(A + 1, 0, 0)
    # 4. 没有硬币的时候
    elif A == 0 and B == 0 and C == 0:
        return 0
