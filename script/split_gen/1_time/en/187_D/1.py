def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB = sorted(AB, key=lambda x: x[0] + x[1], reverse=True)
    diff = 0
    ans = 0
    for i in range(N):
        diff += AB[i][0]
        ans += 1
        if diff > sum(AB[i][1] for i in range(i+1, N)):
            break
    print(ans)
