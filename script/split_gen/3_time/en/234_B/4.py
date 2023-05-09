def main():
    n = int(input())
    points = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5)
    print(ans)
