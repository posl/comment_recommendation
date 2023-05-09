def main():
    # N: number of cities
    # M: number of roads
    N, M = map(int, input().split())
    # A: city A_i
    # B: city B_i
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # count: number of pairs of cities that can be the origin and destination
    count = 0
    for i in range(N):
        count += N-1
        for j in range(M):
            if A[j] == i+1 or B[j] == i+1:
                count -= 1
    print(count)

if __name__ == '__main__':
    main()