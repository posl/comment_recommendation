def solve(S,T):
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    return count

if __name__ == '__main__':
    solve()