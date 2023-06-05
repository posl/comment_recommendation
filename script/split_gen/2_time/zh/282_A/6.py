def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #N, K, D = 4, 2, 2
    #A = [1, 2, 3, 4]
    #N, K, D = 3, 1, 2
    #A = [1, 3, 5]
    print(N, K, D)
    print(A)
    print()
    S = []
    for i in range(N):
        for j in range(N):
            if i != j:
                S.append(A[i] + A[j])
    print(S)
    print()
    S = list(set(S))
    print(S)
    print()
    S.sort()
    print(S)
    print()
    S = [x for x in S if x % D != 0]
    print(S)
    print()
    if len(S) == 0:
        print(-1)
    else:
        print(S[-1])
