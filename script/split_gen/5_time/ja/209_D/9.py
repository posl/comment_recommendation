def main():
    N, Q = map(int, input().split())
    routes = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        routes.append((a, b))
    for _ in range(Q):
        c, d = map(int, input().split())
        if (c, d) in routes or (d, c) in routes:
            print('Road')
        else:
            print('Town')
