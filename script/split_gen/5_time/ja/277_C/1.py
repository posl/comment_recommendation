def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    for i in range(N):
        if ans < AB[i][0]:
            ans = AB[i][1]
    print(ans)
