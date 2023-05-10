def main():
    #n = int(input())
    #a, b = map(int, input().split())
    #s = input()
    n = int(input())
    xyz = []
    for i in range(n):
        x, y, h = map(int, input().split())
        xyz.append([x, y, h])
    xyz.sort(key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            H = xyz[0][2] + abs(xyz[0][0] - cx) + abs(xyz[0][1] - cy)
            if all([max(H - abs(xyz[i][0] - cx) - abs(xyz[i][1] - cy), 0) == xyz[i][2] for i in range(n)]):
                print(cx, cy, H)
                exit()
