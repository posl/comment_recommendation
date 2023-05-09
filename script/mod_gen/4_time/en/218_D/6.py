def solve():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    points = set(points)
    answer = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if (x1, y2) in points and (x2, y1) in points:
                answer += 1
    print(answer)

if __name__ == '__main__':
    solve()