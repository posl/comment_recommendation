def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    route = [1]
    next = A[0]
    while True:
        if next == 1:
            break
        else:
            route.append(next)
            next = A[next-1]
    if K < len(route):
        print(route[K])
    else:
        K -= len(route)
        route.pop(0)
        K %= len(route)
        print(route[K])

if __name__ == '__main__':
    main()