def get_input():
    n, c = map(int, input().split())
    plans = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        plans.append((a, b, c))
    return n, c, plans
