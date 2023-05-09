def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = []
    for i in a:
        ans.append(n-1-d[i]+1)
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()