def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ans = -10**9
    for i in range(n):
        now = i
        score = 0
        num = 0
        while num < k:
            now = p[now]-1
            score += c[now]
            num += 1
            ans = max(ans,score)
            if score > 0 and num < k:
                score += (k//num-1)*score
                num += (k//num-1)*num
    print(ans)

if __name__ == '__main__':
    main()