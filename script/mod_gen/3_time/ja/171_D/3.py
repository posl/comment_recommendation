def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    sum_a = sum(A)
    for i in range(Q):
        count = A.count(B[i])
        sum_a += count * (C[i] - B[i])
        print(sum_a)

if __name__ == '__main__':
    main()