def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[i] == x:
            continue
        ans.append(str(a[i]))
    print(' '.join(ans))

if __name__ == '__main__':
    main()