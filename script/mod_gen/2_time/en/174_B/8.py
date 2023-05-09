def get_input():
    n, d = map(int, input().split())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    return n, d, points

if __name__ == '__main__':
    get_input()