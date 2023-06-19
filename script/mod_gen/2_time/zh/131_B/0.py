def main():
    n, l = map(int, input().split())
    if l >= 0:
        ans = sum(list(range(l+1, l+n)))
    elif l+n-1 <= 0:
        ans = sum(list(range(l, l+n)))
    else:
        ans = sum(list(range(l, l+n-1))) + l+n-1
    print(ans)

if __name__ == '__main__':
    main()