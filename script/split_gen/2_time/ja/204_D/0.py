def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = T[0]
    for i in range(1, N):
        ans += T[i]
    print(ans)
