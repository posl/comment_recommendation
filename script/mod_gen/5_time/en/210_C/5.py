def main():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    result = 0
    color = {}
    for i in range(K):
        if C[i] not in color:
            color[C[i]] = 0
        color[C[i]] += 1
    result = len(color)
    for i in range(K, N):
        if C[i - K] in color:
            color[C[i - K]] -= 1
            if color[C[i - K]] == 0:
                del color[C[i - K]]
        if C[i] not in color:
            color[C[i]] = 0
        color[C[i]] += 1
        result = max(result, len(color))
    print(result)

if __name__ == '__main__':
    main()