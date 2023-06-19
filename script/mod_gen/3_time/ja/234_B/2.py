def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, (xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2)
    print(ans**0.5)
main()
