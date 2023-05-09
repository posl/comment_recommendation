def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [0] * m
    for i in range(m):
        xy[i] = list(map(int, input().split()))
    for i in range(m):
        t = t - (xy[i][0] - xy[i-1][0]) - xy[i][1]
    if t <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()