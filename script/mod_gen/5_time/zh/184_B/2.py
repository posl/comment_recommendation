def solve(n,x,s):
    score = x
    for i in range(n):
        if s[i] == 'o':
            score += 1
        else:
            if score > 0:
                score -= 1
    return score

if __name__ == '__main__':
    solve()