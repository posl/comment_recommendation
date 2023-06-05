def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [1, 5, 3, 2, 5, 2, 3, 1]
    # N = 8
    # A = [1, 2, 3, 4, 1, 2, 3]
    # N = 7
    # A = [200000]
    # N = 1
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    # print(d)
    result = 0
    for i in d:
        if d[i] % 2 == 1:
            result += 1
    print(result)

if __name__ == '__main__':
    main()