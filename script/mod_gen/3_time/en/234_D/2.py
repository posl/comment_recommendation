def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    Q = [P[i] for i in range(K)]
    Q.sort()
    print(Q[K-1])
    for i in range(K, N):
        if P[i] <= Q[0]:
            continue
        for j in range(K):
            if P[i] <= Q[j]:
                Q.insert(j, P[i])
                Q.pop(0)
                break
        print(Q[K-1])

if __name__ == '__main__':
    main()