def get_input():
    n,d = [int(x) for x in input().split()]
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    return n,d,points
