def solve(n, s, t):
    for i in range(n):
        if s[i][0] != t[i][0] or s[i][1] != t[i][1]:
            break
    else:
        return 'Yes'
    for i in range(n):
        for j in range(n):
            if s[(i + j) % n][0] != t[j][0] or s[(i + j) % n][1] != t[j][1]:
                break
        else:
            return 'Yes'
    for i in range(n):
        for j in range(n):
            if s[(i + j) % n][0] != t[-j][0] or s[(i + j) % n][1] != t[-j][1]:
                break
        else:
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    solve()