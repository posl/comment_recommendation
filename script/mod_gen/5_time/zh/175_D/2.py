def solve(n,k,p,c):
    maxScore = -10000000000
    for i in range(n):
        next = p[i]-1
        score = c[next]
        for j in range(k-1):
            next = p[next]-1
            score += c[next]
        if score > maxScore:
            maxScore = score
    return maxScore

if __name__ == '__main__':
    solve()