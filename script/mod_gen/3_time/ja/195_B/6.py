def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_n = 0
    max_n = 0
    for i in range(1, W+1):
        if A * i <= W <= B * i:
            min_n = i
            break
    for i in range(W, 0, -1):
        if A * i <= W <= B * i:
            max_n = i
            break
    if min_n == 0 and max_n == 0:
        print("UNSATISFIABLE")
    else:
        print(min_n, max_n)

if __name__ == '__main__':
    main()