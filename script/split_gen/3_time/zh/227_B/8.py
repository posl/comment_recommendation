def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if S[i] % 6 == 0:
            continue
        elif S[i] % 6 == 2:
            ans += 1
        elif S[i] % 6 == 4:
            ans += 1
        elif S[i] % 6 == 5:
            ans += 1
        else:
            continue
    print(ans)
