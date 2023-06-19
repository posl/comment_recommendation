def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = (S[i] + A[i]) % 200
    D = {}
    for i in range(N+1):
        if S[i] not in D:
            D[S[i]] = []
        D[S[i]].append(i)
    for k in D:
        if len(D[k]) > 1:
            print('Yes')
            print(len(D[k])-1, *D[k][1:])
            print(len(D[k])-1, *D[k][:-1])
            return
    print('No')
    return
main()
