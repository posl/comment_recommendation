def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    #print(N)
    #print(P)
    #print(Q)
    def permutation(N, P):
        if N == 1:
            return [P]
        ret = []
        for i in range(N):
            for p in permutation(N-1, P[:i] + P[i+1:]):
                ret.append([P[i]] + p)
        return ret
    def calc(N, P, Q):
        P_permutation = permutation(N, P)
        Q_permutation = permutation(N, Q)
        P_permutation.sort()
        Q_permutation.sort()
        P_permutation_index = 0
        Q_permutation_index = 0
        for i in range(len(P_permutation)):
            if P_permutation[i] == P:
                P_permutation_index = i
            if Q_permutation[i] == Q:
                Q_permutation_index = i
        print(abs(P_permutation_index - Q_permutation_index))
    calc(N, P, Q)
