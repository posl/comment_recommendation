def main():
    N = int(input())
    S = input()
    W = [int(w) for w in input().split()]
    ans = 0
    for i in range(1, N):
        if S[i - 1] == '0' and S[i] == '1':
            ans += 1
    if S[-1] == '0':
        ans += 1
    print(ans)
