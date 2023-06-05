def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # S = list(S)
    # for q in queries:
    #     if q[0] == 1:
    #         for _ in range(q[1]):
    #             S.insert(0, S.pop())
    #     else:
    #         print(S[q[1]-1])
    S = S*2
    for q in queries:
        if q[0] == 1:
            S = S[N-q[1]:2*N-q[1]]
        else:
            print(S[q[1]-1])

if __name__ == '__main__':
    main()