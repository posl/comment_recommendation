def main():
    n = int(input())
    h = list(map(int, input().split()))
    #print(n)
    #print(h)
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()