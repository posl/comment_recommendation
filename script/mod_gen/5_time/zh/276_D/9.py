def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        is_even = True
        for i in range(N):
            if A[i] % 2 != 0:
                is_even = False
                break
        if is_even:
            for i in range(N):
                A[i] = A[i] // 2
            count += 1
        else:
            break
    while True:
        is_multiple_of_three = True
        for i in range(N):
            if A[i] % 3 != 0:
                is_multiple_of_three = False
                break
        if is_multiple_of_three:
            for i in range(N):
                A[i] = A[i] // 3
            count += 1
        else:
            break
    for i in range(N):
        if A[i] != 1:
            count = -1
            break
    print(count)

if __name__ == '__main__':
    main()