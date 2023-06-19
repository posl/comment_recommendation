def get_input():
    num = int(raw_input())
    points = []
    for i in range(num):
        points.append(map(int, raw_input().split()))
    return points

if __name__ == '__main__':
    get_input()