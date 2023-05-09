def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min_oranges = 0
    max_oranges = 0
    for i in range(1, W + 1):
        if W % i == 0 and A <= W / i <= B:
            min_oranges = i
            break
    for i in range(W, 0, -1):
        if W % i == 0 and A <= W / i <= B:
            max_oranges = i
            break
    if min_oranges == 0 and max_oranges == 0:
        print('UNSATISFIABLE')
    else:
        print(min_oranges, max_oranges)

if __name__ == '__main__':
    main()