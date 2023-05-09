def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dictA = {}
    dictB = {}
    for i in range(N):
        dictA[A[i]] = i
        dictB[B[i]] = i
    count = 0
    for i in range(N):
        if A[i] in dictB and dictB[A[i]] == i:
            count += 1
    print(count)
    count = 0
    for i in range(N):
        if A[i] in dictB and dictB[A[i]] != i:
            count += 1
    print(count)

if __name__ == '__main__':
    main()