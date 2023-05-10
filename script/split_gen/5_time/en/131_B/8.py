def main():
    n, l = [int(x) for x in input().split()]
    if l >= 0:
        print(sum([l+i for i in range(1, n)]))
    elif -l >= n:
        print(sum([l+i for i in range(1, n)]))
    else:
        print(sum([l+i for i in range(1, n)])-min([l+i for i in range(1, n)]))
