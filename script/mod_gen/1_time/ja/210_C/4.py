def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0
    tmp = 0
    dic = {}
    for i in range(N):
        if i < K:
            if c[i] not in dic:
                dic[c[i]] = 1
                tmp += 1
            else:
                dic[c[i]] += 1
        else:
            if c[i] not in dic:
                dic[c[i]] = 1
                tmp += 1
            else:
                dic[c[i]] += 1
            if c[i-K] in dic:
                dic[c[i-K]] -= 1
                if dic[c[i-K]] == 0:
                    tmp -= 1
            if tmp > ans:
                ans = tmp
    print(ans)

if __name__ == '__main__':
    main()