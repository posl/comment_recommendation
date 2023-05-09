def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    if S == S[::-1]:
        print(ans)
        return
    for i in range(N):
        if S[i] != S[N-1-i]:
            ans = A
            break
    if ans == 0:
        ans = B
    print(ans)
    return
