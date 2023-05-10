def get_input():
    n, m = map(int, input().split())
    bulbs = []
    for i in range(m):
        bulbs.append([int(x) for x in input().split()])
    p = [int(x) for x in input().split()]
    return n, m, bulbs, p
