def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [i - 1 for i in p]
    ans = -float('inf')
    for i in range(n):
        score = 0
        cnt = 0
        v = i
        while True:
            v = p[v]
            score += c[v]
            cnt += 1
            if cnt == k:
                break
            if score > ans:
                ans = score
            if v == i:
                break
    print(ans)

if __name__ == '__main__':
    main()