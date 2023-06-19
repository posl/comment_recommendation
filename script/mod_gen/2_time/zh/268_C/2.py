def main():
    n = int(input())
    p = list(map(int,input().split()))
    p.insert(0,0)
    p.append(0)
    ans = 0
    for i in range(1,n+1):
        if p[i-1] == i-1 or p[i+1] == i-1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()