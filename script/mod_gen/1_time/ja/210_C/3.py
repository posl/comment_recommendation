def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    candy = dict()
    for i in range(K):
        if c[i] in candy:
            candy[c[i]] += 1
        else:
            candy[c[i]] = 1
    max_candy = len(candy)
    for i in range(K, N):
        if c[i] in candy:
            candy[c[i]] += 1
        else:
            candy[c[i]] = 1
        if candy[c[i-K]] == 1:
            candy.pop(c[i-K])
        else:
            candy[c[i-K]] -= 1
        if len(candy) > max_candy:
            max_candy = len(candy)
    print(max_candy)

if __name__ == '__main__':
    main()