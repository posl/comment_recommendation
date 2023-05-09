def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = list()
    C = list()
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    sumA = sum(A)
    for i in range(Q):
        count = A.count(B[i])
        sumA -= B[i] * count
        sumA += C[i] * count
        print(sumA)

if __name__ == '__main__':
    main()