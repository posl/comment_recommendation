def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # print(n, k, p)
    for i in range(k-1, n):
        # print(i, k, n)
        print(max(p[i-k+1:i+1]))

if __name__ == '__main__':
    main()