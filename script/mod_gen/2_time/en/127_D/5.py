def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort()
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in BC:
        for j in range(b):
            if i < N and A[i] < c:
                A[i] = c
                i += 1
            else:
                break
    print(sum(A))

if __name__ == '__main__':
    main()