def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    ans = T[-1]
    for i in range(N-1):
        ans += T[i]
    print(ans)
