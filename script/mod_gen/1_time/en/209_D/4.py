def main():
    N, Q = map(int, input().split())
    road = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        road[a].append(b)
        road[b].append(a)
    for _ in range(Q):
        c, d = map(int, input().split())
        if (N-1) % 2 == 0:
            print("Town")
        else:
            if len(road[c]) % 2 != len(road[d]) % 2:
                print("Town")
            else:
                print("Road")

if __name__ == '__main__':
    main()