def main():
    n, q = map(int, input().split())
    road = [[0 for i in range(n)] for j in range(n)]
    for i in range(n-1):
        a, b = map(int, input().split())
        road[a-1][b-1] = 1
        road[b-1][a-1] = 1
    for i in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if road[c][d] == 1:
            print("Road")
        else:
            print("Town")
