def solve(N, S):
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(' '.join(map(str, A)))

if __name__ == '__main__':
    solve()