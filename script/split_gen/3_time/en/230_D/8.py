def main():
    import sys
    input = sys.stdin.readline
    N, D = map(int, input().split())
    wall = []
    for i in range(N):
        L, R = map(int, input().split())
        wall.append([L, R])
    wall.sort()
    # print(wall)
    count = 0
    for i in range(N):
        if wall[i][0] > D:
            count += 1
            D = wall[i][1]
        else:
            D = max(D, wall[i][1])
    print(count + 1)
