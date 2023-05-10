def main():
    n = int(input())
    xyz = [list(map(int, input().split())) for i in range(n)]
    for i in range(101):
        for j in range(101):
            h = xyz[0][2] + abs(xyz[0][0] - i) + abs(xyz[0][1] - j)
            if all(max(h - abs(xyz[k][0] - i) - abs(xyz[k][1] - j), 0) == xyz[k][2] for k in range(n)):
                print(i, j, h)
                break
