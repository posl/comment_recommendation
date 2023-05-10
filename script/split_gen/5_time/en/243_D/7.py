def main():
    N, X = map(int, input().split())
    S = input()
    #print(N, X, S)
    ans = X
    for i in range(N):
        if S[i] == 'L':
            ans = ans * 2 - 1
        elif S[i] == 'R':
            ans = ans * 2 + 1
        else:
            ans = ans // 2
    print(ans)
