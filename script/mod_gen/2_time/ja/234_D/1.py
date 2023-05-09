def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    C = [0] * N
    for i in range(N):
        C[P[i]] = i
    #print(P)
    #print(C)
    ans = []
    for i in range(K, N):
        #print(i)
        #print(C)
        #print(P)
        #print(P[i])
        #print(C[P[i]])
        #print(P[i] - C[P[i]])
        if P[i] - C[P[i]] >= K:
            ans.append(0)
        else:
            ans.append(1)
    print('
'.join(map(str, ans)))

if __name__ == '__main__':
    main()