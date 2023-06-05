def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    color = {}
    for i in range(K):
        if c[i] in color:
            color[c[i]] += 1
        else:
            color[c[i]] = 1
    # print(color)
    ans = len(color)
    for i in range(N-K):
        if c[i] in color:
            color[c[i]] -= 1
            if color[c[i]] == 0:
                del color[c[i]]
        if c[i+K] in color:
            color[c[i+K]] += 1
        else:
            color[c[i+K]] = 1
        # print(color)
        ans = max(ans, len(color))
    print(ans)

if __name__ == '__main__':
    main()