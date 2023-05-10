def solve(s,t):
    min = len(t)
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                cnt += 1
        if cnt < min:
            min = cnt
    return min

if __name__ == '__main__':
    solve()