def get_input():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    return n, points

if __name__ == '__main__':
    get_input()