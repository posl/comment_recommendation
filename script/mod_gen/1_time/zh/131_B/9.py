def main():
    n,l = map(int, input().split())
    res = 0
    if l >= 0:
        res = sum(range(l+1, l+n))
    elif l+n <= 0:
        res = sum(range(l, l+n))
    else:
        res = sum(range(l+1, 0)) + sum(range(1, l+n))
    print(res)

if __name__ == '__main__':
    main()