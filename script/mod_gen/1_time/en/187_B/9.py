def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    slopes = [0] * N
    for i in range(N):
        for j in range(N):
            if i < j:
                if points[i][0] != points[j][0]:
                    slopes[i] += 1
                    slopes[j] += 1
    ans = 0
    for s in slopes:
        ans += s
    print(ans // 2)

if __name__ == '__main__':
    main()