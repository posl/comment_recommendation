def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(n):
        next = p[i] - 1
        score = 0
        cnt = 0
        while cnt < k:
            cnt += 1
            score += c[next]
            next = p[next] - 1
            ans = max(ans, score)
            if next == i:
                break
    print(ans)
main()

if __name__ == '__main__':
    main()