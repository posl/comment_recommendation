def main():
    # input
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    # compute
    # output
    print(min(sum(a), n*(l+r)))

if __name__ == '__main__':
    main()