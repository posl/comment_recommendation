def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, max(A)+1):
        cnt = 0
        for a in A:
            if a >= x:
                cnt += 1
            else:
                ans = max(ans, cnt*x)
                cnt = 0
        ans = max(ans, cnt*x)
    print(ans)

if __name__ == '__main__':
    main()