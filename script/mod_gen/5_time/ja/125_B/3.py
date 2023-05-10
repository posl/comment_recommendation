def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        tmp = v[i] - c[i]
        if tmp > 0:
            ans += tmp
    print(ans)

if __name__ == '__main__':
    main()