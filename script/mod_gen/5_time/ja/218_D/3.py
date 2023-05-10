def get_input():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    return n, x, y

if __name__ == '__main__':
    get_input()