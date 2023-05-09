def main():
    A, B, W = map(int, input().split())
    W = W * 1000
    min = 1000000000
    max = 0
    for i in range(1, 1000000000):
        if A * i <= W <= B * i:
            if min > i:
                min = i
            if max < i:
                max = i
    if min == 1000000000:
        print("UNSATISFIABLE")
    else:
        print(min, max)

if __name__ == '__main__':
    main()