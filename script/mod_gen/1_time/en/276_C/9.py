def getSmallestPermutation(N, P):
    P = [p - 1 for p in P]
    Q = [0] * N
    Q[0] = P[0]
    for i in range(1, N):
        if P[i] < P[i - 1]:
            Q[i] = P[i]
        else:
            Q[i] = P[i] - 1
    return [q + 1 for q in Q]
N = int(input())
P = list(map(int, input().split()))
Q = getSmallestPermutation(N, P)
print(" ".join(map(str, Q)))

if __name__ == '__main__':
    getSmallestPermutation()