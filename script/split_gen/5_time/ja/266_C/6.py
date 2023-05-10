def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    if (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0]) > 0:
        if (b[0] - c[0]) * (d[1] - c[1]) - (b[1] - c[1]) * (d[0] - c[0]) > 0:
            if (c[0] - d[0]) * (a[1] - d[1]) - (c[1] - d[1]) * (a[0] - d[0]) > 0:
                if (d[0] - a[0]) * (b[1] - a[1]) - (d[1] - a[1]) * (b[0] - a[0]) > 0:
                    print('Yes')
                    exit()
    print('No')
