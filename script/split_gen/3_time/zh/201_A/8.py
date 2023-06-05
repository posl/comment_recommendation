def main():
    a = [int(x) for x in input().split()]
    a.sort()
    if a[2]-a[1] == a[1]-a[0]:
        print('Yes')
    else:
        print('No')
