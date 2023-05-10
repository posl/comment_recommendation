def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = []
    for i in range(N):
        C.append(A[i] + B[i])
    C.sort()
    C.reverse()
    sum = 0
    count = 0
    for i in range(N):
        sum += C[i]
        count += 1
        if sum > sum / 2:
            break
    print(count)

if __name__ == '__main__':
    main()