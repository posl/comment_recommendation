def main():
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    if a[1] - a[0] == a[2] - a[1]:
        print('Yes')
    else:
        print('No')
