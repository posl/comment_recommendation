def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    S = sum(A)
    count = [0] * (10 ** 5 + 1)
    for a in A:
        count[a] += 1
    for i in range(Q):
        count[B[i]] -= 1
        count[C[i]] += 1
        S += (C[i] - B[i]) * count[B[i]]
        print(S)

if __name__ == '__main__':
    main()