def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        if AB[i][0] < ans:
            continue
        ans = AB[i][1] - 1
    print(ans)
