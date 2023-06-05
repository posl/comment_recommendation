def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    # print(n, k, x)
    res = 10**8
    for i in range(n-k+1):
        if x[i] <= 0 and x[i+k-1] <= 0:
            res = min(res, abs(x[i]))
        elif x[i] >= 0 and x[i+k-1] >= 0:
            res = min(res, abs(x[i+k-1]))
        else:
            res = min(res, 2*min(abs(x[i]), abs(x[i+k-1])) + max(abs(x[i]), abs(x[i+k-1])))
    print(res)

if __name__ == '__main__':
    main()