def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = 1001
    max = 0
    for i in range(1, W + 1):
        if A <= i <= B:
            if W % i == 0:
                if min > W // i:
                    min = W // i
                if max < W // i:
                    max = W // i
    if min == 1001:
        print('UNSATISFIABLE')
    else:
        print(min, max)

if __name__ == '__main__':
    main()