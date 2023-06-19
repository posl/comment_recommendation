def get_input():
    n, w = map(int, input().split())
    cheese = []
    for _ in range(n):
        cheese.append(list(map(int, input().split())))
    return n, w, cheese
