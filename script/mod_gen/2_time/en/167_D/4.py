def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    A.insert(0, 0)
    route = [1]
    current = 1
    for i in range(K):
        current = A[current]
        if current in route:
            break
        route.append(current)
    if len(route) == K:
        print(current)
    else:
        print(route[(K - len(route)) % (len(route) - route.index(current)) + route.index(current)])

if __name__ == '__main__':
    main()