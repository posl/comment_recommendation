def main():
    A, B, W = map(int, input().split())
    W *= 1000
    max_n = 0
    min_n = 1000000
    for i in range(1, 1000001):
        if A*i <= W <= B*i:
            max_n = max(max_n, i)
            min_n = min(min_n, i)
    if max_n == 0:
        print("UNSATISFIABLE")
    else:
        print(min_n, max_n)

if __name__ == '__main__':
    main()