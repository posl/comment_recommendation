def main():
    a = input().rstrip().split()
    a.sort()
    if int(a[2]) - int(a[1]) == int(a[1]) - int(a[0]):
        print('Yes')
    else:
        print('No')
