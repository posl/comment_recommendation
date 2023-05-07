def main():
    # input
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    BC = [list(map(int, input().split())) for _ in range(q)]
    # compute
    sumA = sum(A)
    cntA = [0] * 100001
    for a in A:
        cntA[a] += 1
    # output
    for b, c in BC:
        sumA += (c-b) * cntA[b]
        cntA[c] += cntA[b]
        cntA[b] = 0
        print(sumA)

if __name__ == '__main__':
    main()