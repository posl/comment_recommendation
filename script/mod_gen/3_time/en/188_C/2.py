def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(a, i) for i, a in enumerate(A)]
    A.sort()
    for i in range(N):
        B = []
        for j in range(0, len(A), 2):
            B.append(A[j])
        A = B
    print(A[0][1] + 1)

if __name__ == '__main__':
    main()