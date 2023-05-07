def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    AB.append([10**9+1, 0])
    ans = 0
    for i in range(N):
        ans += (AB[i+1][0] - AB[i][0]) * min(C, AB[i][1])
    print(ans)
