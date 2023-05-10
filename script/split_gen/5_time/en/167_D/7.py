def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    route = [1]
    next = A[0]
    while not next in route:
        route.append(next)
        next = A[next-1]
    cycle_start = route.index(next)
    cycle = route[cycle_start:]
    if K < cycle_start:
        print(route[K])
    else:
        print(cycle[(K-cycle_start)%len(cycle)])
