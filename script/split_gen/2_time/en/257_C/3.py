def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if S[i] != S[i-1]:
            ans += 1
    if ans == 0:
        print(N)
    elif ans == 1:
        print(N-1)
    else:
        print(ans)
