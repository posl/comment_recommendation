def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n-1, -1, -1):
        if sum(a[i::i+1]) % 2 != a[i]:
            ans.append(i+1)
            a[i] = 1
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()