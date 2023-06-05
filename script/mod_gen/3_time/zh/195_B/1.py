def main():
    A, B, W = map(int, input().split())
    W *= 1000
    min = 0
    max = 0
    for i in range(1, 1000001):
        if A <= W / i <= B:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

if __name__ == '__main__':
    main()