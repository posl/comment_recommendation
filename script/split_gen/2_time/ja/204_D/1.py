def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = 0
    for i in range(N-1):
        ans += T[i]
    ans += T[-1]
    print(ans)
