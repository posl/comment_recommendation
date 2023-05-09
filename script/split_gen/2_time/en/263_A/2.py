def main():
    a = [int(x) for x in input().split()]
    if (a[0] == a[1] == a[2] and a[3] == a[4]) or (a[0] == a[1] and a[2] == a[3] == a[4]):
        print('Yes')
    else:
        print('No')
