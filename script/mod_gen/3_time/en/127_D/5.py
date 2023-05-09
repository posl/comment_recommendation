def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort(reverse=True)
    B, C = zip(*sorted(zip(B, C), key=lambda x: x[1], reverse=True))
    i = 0
    for b, c in zip(B, C):
        for _ in range(b):
            if i >= N:
                break
            if A[i] < c:
                A[i] = c
                i += 1
            else:
                break
    print(sum(A))

if __name__ == '__main__':
    main()