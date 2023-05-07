def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N + 1]
    B = []
    for i in range(M + 1):
        B.append(A[i + 1] - A[i] - 1)
    B.sort()
    print(sum(B[:M + 1 - B.count(0)]))

if __name__ == '__main__':
    main()