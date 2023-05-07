def getNthSmallestDivisibleBy100(D,N):
    if D == 0:
        return N
    elif D == 1:
        return 100 * N
    elif D == 2:
        return 10000 * N
D,N = input().split()
D = int(D)
N = int(N)

if __name__ == '__main__':
    getNthSmallestDivisibleBy100()