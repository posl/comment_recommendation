def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = -1
    max = 0
    for i in range(1, W+1):
        if A * i <= W and W <= B * i:
            if min == -1:
                min = i
            max = i
    if min == -1:
        print('UNSATISFIABLE')
    else:
        print(min, max)

if __name__ == '__main__':
    main()