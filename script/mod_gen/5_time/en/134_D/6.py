def main():
    # get input
    n = int(input())
    a = list(map(int, input().split()))
    # solve
    b = [0] * n
    for i in range(n-1, -1, -1):
        s = sum(b[i::i+1]) % 2
        if s != a[i]:
            b[i] = 1
    # output
    ans = [i+1 for i in range(n) if b[i] == 1]
    print(len(ans))
    if len(ans) > 0:
        print(*ans)

if __name__ == '__main__':
    main()