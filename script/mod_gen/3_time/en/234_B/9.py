def main():
    import sys
    import math
    N = int(sys.stdin.readline())
    xys = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    max_dist = -1
    for i in range(N):
        for j in range(i + 1, N):
            dist = math.sqrt((xys[i][0] - xys[j][0]) ** 2 + (xys[i][1] - xys[j][1]) ** 2)
            if dist > max_dist:
                max_dist = dist
    print(max_dist)

if __name__ == '__main__':
    main()