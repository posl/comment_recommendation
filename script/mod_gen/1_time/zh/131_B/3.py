def main():
    n, l = map(int, input().split())
    if l >= 0:
        print(sum(range(l+1, l+n)))
    elif l+n <= 0:
        print(sum(range(l, l+n)))
    else:
        print(sum(range(l, 0)) + sum(range(1, l+n)))

if __name__ == '__main__':
    main()