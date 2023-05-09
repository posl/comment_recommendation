def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(M)]
    A.sort(reverse = True)
    BC.sort(key = lambda x: x[1], reverse = True)
    idx = 0
    for b, c in BC:
        for i in range(b):
            if idx >= N:
                break
            if A[idx] < c:
                A[idx] = c
                idx += 1
            else:
                break
    print(sum(A))

if __name__ == '__main__':
    main()