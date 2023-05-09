def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i
    count = 0
    for i in range(N):
        if B[i] < i:
            continue
        for j in range(i + 1, N):
            if B[j] < i:
                continue
            if B[j] < B[i]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()