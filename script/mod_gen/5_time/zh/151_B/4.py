def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    s = sum(A)
    ans = -1
    for i in range(K+1):
        if (s + i) / N >= M:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()