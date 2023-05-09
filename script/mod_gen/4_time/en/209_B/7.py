def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a_odd = a[::2]
    a_even = a[1::2]
    if sum(a_odd) - len(a_odd) + len(a_even) >= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()