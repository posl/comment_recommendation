def get_input():
    n = int(input())
    xy = []
    for i in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    return n, xy

if __name__ == '__main__':
    get_input()