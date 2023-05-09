def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    p.insert(0,0)
    ans = 0
    for i in range(1,n+1):
        ans = max(ans, p[i])
        for j in range(ans):
            p[i] = p[p[i]]
    print(ans)

if __name__ == '__main__':
    main()