def main():
    A, B, W = map(int, input().split())
    W = W * 1000
    min_n = 10 ** 9
    max_n = -1
    for i in range(A, B + 1):
        if W % i == 0:
            min_n = min(min_n, W // i)
            max_n = max(max_n, W // i)
    if min_n == 10 ** 9:
        print("UNSATISFIABLE")
    else:
        print(min_n, max_n)

if __name__ == '__main__':
    main()