def main():
    N,K = map(int,input().split())
    S = [input() for _ in range(N)]
    c = [0]*26
    for s in S:
        for i in range(26):
            if chr(97+i) in s:
                c[i] += 1
    c.sort(reverse=True)
    ans = 0
    for i in range(K):
        ans += c[i]
    print(ans)
main()

if __name__ == '__main__':
    main()