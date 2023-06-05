def main():
    n, l = map(int, input().split())
    if l >= 0:
        ans = sum(range(l+1, l+n))
    elif l+n-1 <= 0:
        ans = sum(range(l, l+n-1))
    else:
        ans = sum(range(l+1, 0)) + sum(range(1, l+n))
    print(ans)

if __name__ == '__main__':
    main()