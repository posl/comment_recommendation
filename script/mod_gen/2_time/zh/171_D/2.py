def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    B = []
    C = []
    for i in range(q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    sum = 0
    for i in range(n):
        sum += A[i]
    for i in range(q):
        sum += (C[i] - B[i]) * A.count(B[i])
        print(sum)
        sum = sum - (C[i] - B[i]) * A.count(B[i])
        A = list(map(lambda x: C[i] if x == B[i] else x, A))

if __name__ == '__main__':
    main()