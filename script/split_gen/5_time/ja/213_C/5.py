def main():
    H, W, N = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB = sorted(AB, key=lambda x: x[0])
    AB = sorted(AB, key=lambda x: x[1])
    print(AB)
    for i in range(N):
        print(AB[i][0], AB[i][1])
