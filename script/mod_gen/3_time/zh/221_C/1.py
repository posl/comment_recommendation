def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        a = str(i)
        b = str(n - i)
        if '0' in a or '0' in b:
            continue
        ans = max(ans, int(a) * int(b))
    print(ans)

if __name__ == '__main__':
    main()