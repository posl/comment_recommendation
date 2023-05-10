def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append((10**9+1, 0))
    ans = [0]*(N+1)
    day = 0
    for i in range(N):
        if day < AB[i][0]:
            day = AB[i][0]
        ans[AB[i][1]] += AB[i][0]-day+1
        ans[AB[i+1][1]] -= AB[i][0]-day+1
        day += AB[i][1]
    print(*ans[:-1])
