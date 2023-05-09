def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for i in range(0, min(n, k)+1):
        for l in range(0, min(n, k)-i+1):
            r = k - i - l
            tmp = v[:i] + v[n-l:]
            tmp.sort()
            for j in range(min(r, len(tmp))):
                if tmp[j] < 0:
                    tmp[j] = 0
            ans = max(ans, sum(tmp))
    print(ans)

if __name__ == '__main__':
    main()