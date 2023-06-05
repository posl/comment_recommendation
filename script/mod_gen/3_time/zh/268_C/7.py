def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]] = i
    ans = 0
    cnt = 0
    for i in range(n):
        if q[i] > cnt:
            cnt = q[i]
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()