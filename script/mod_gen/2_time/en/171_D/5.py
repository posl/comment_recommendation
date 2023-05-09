def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for _ in range(Q):
        b, c = list(map(int, input().split()))
        B.append(b)
        C.append(c)
    sum_A = sum(A)
    count_B = [0] * (10**5 + 1)
    for a in A:
        count_B[a] += 1
    for i in range(Q):
        sum_A += (C[i] - B[i]) * count_B[B[i]]
        count_B[C[i]] += count_B[B[i]]
        count_B[B[i]] = 0
        print(sum_A)

if __name__ == '__main__':
    main()