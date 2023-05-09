def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K)+1):
        for j in range(min(N, K)-i+1):
            if i+j > N:
                continue
            l = V[:i]
            r = V[N-j:]
            l.sort()
            r.sort()
            s = sum(l)
            s += sum(r)
            for k in range(min(K-i-j, i+j)):
                if l[k] < 0:
                    s -= l[k]
            ans = max(ans, s)
    print(ans)
main()

if __name__ == '__main__':
    main()