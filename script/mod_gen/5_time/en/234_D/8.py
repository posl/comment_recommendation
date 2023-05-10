def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p = [0] + p
    p2 = [0] * (n+1)
    for i in range(1, n+1):
        p2[i] = p2[i-1] + p[i]
    for i in range(k, n+1):
        print(p2[i] - p2[i-k])

if __name__ == '__main__':
    main()