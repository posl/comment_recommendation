def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_oranges = 0
    max_oranges = 0
    for i in range(1, W + 1):
        if A <= i <= B:
            if min_oranges == 0:
                min_oranges = i
            max_oranges = i
    if min_oranges == 0:
        print("UNSATISFIABLE")
    else:
        print(W // max_oranges, W // min_oranges)

if __name__ == '__main__':
    main()