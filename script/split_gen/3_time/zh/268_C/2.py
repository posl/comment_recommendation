def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if P[i] == i:
            ans += 1
    if ans == N:
        print(N)
    else:
        print(ans+2)
