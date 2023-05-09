def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    max = 0
    for i in range(N-K+1):
        tmp = c[i:i+K]
        tmp = set(tmp)
        if max < len(tmp):
            max = len(tmp)
    print(max)

if __name__ == '__main__':
    main()