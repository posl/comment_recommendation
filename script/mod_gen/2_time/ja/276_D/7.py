def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            else:
                break
        else:
            count += 1
            continue
        break
    if A == [1] * N:
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    main()