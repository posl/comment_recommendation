def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    print('Yes' if a[-1] < b[0] else 'No')
