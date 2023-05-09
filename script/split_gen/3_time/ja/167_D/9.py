def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [x - 1 for x in A]
    # 1回目の移動
    next = A[0]
    # 2回目以降の移動
    route = [0]
    while True:
        next = A[next]
        if next in route:
            break
        route.append(next)
    # K回目の移動
    K = (K - 1) % len(route)
    print(route[K] + 1)
