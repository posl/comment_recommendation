def main():
    x = input()
    m = int(input())
    d = int(max(x))
    ans = 0
    for n in range(d+1, m+1):
        if int(x, n) <= m:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()