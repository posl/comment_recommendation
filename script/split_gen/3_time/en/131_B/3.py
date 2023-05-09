def main():
    n, l = map(int, input().split())
    if l <= 0 and 0 <= l+n-1:
        print(sum(range(l, l+n)))
    elif l+n-1 < 0:
        print(sum(range(l, l+n-1)))
    else:
        print(sum(range(l+1, l+n)))
