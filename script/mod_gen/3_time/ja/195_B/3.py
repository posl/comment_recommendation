def main():
    A, B, W = map(int, input().split())
    min = 1000
    max = 0
    for i in range(1, 1001):
        if A * i <= W * 1000 <= B * i:
            if min > i:
                min = i
            if max < i:
                max = i
    if min == 1000:
        print("UNSATISFIABLE")
    else:
        print(min, max)

if __name__ == '__main__':
    main()