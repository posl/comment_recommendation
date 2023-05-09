def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(n)]
    xyr.append([sx, sy, 0])
    xyr.append([tx, ty, 0])
    ans = "No"
    for i in range(n + 1):
        for j in range(i + 1, n + 2):
            d = ((xyr[i][0] - xyr[j][0]) ** 2 + (xyr[i][1] - xyr[j][1]) ** 2) ** 0.5
            if d <= xyr[i][2] + xyr[j][2]:
                ans = "Yes"
    print(ans)
main()
