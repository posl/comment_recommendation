def solve(s,k):
    n = len(s)
    if n == 1:
        return 1
    if n == 2:
        if k == 0:
            return 0
        else:
            return 2
    if n == 3:
        if k == 0:
            return 1
        else:
            return 3
    if n == 4:
        if k == 0:
            return 2
        else:
            return 4
    if k == 0:
        return 1
    if s[0] == '.':
        if s[1] == '.':
            if s[2] == '.':
                if s[3] == '.':
                    return 4
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    if s[1] == '.':
        if s[2] == '.':
            if s[3] == '.':
                return 3
            else:
                return 2
        else:
            return 1
    if s[2] == '.':
        if s[3] == '.':
            return 2
        else:
            return 1
    if s[3] == '.':
        return 1
    return 0
s = input()
k = int(input())
print(solve(s,k))
