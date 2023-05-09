def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            if S[i] == 'a':
                ans += A
            elif S[i] == 'b':
                ans += B
            elif S[i] == 'c':
                ans += A+B
            elif S[N-1-i] == 'a':
                ans += A
            elif S[N-1-i] == 'b':
                ans += B
            elif S[N-1-i] == 'c':
                ans += A+B
    if N%2 == 1 and S[N//2] != 'c':
        if S[N//2] == 'a':
            ans += A
        elif S[N//2] == 'b':
            ans += B
    print(ans)
