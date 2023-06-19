def main():
    n, l = map(int, input().split())
    if n == 2:
        print(l)
    elif l >= 0:
        print(sum(range(l+1, l+n)))
    elif l+n-1 <= 0:
        print(sum(range(l, l+n-1)))
    else:
        print(sum(range(l, 0)) + sum(range(1, l+n-1)))
