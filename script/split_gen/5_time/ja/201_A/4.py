def main():
    a = sorted(list(map(int, input().split())))
    if (a[2] - a[1]) == (a[1] - a[0]):
        print('Yes')
    else:
        print('No')
