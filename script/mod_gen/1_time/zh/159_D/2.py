def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    ans = [0] * N
    for a in A:
        ans[a-1] = N - d[a]
    for a in ans:
        print(a)

if __name__ == '__main__':
    main()