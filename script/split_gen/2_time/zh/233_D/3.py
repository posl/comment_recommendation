def solve(n, x, bags):
    if x == 1:
        return n
    if n == 1:
        for i in range(len(bags)):
            if x in bags[i]:
                return 1
        return 0
    if n == 2:
        count = 0
        for i in range(len(bags[0])):
            if x % bags[0][i] == 0 and x // bags[0][i] in bags[1]:
                count += 1
        return count
    if n == 3:
        count = 0
        for i in range(len(bags[0])):
            for j in range(len(bags[1])):
                if x % bags[0][i] == 0 and x % bags[1][j] == 0 and x // bags[0][i] // bags[1][j] in bags[2]:
                    count += 1
        return count
    return 0
