def main():
    N, Q = map(int, input().split())
    # 1. 1≦ i≦ N に対して、ユーザー i のフォローしているユーザーの集合を F _ i とする。
    # 2. 1≦ i≦ N に対して、ユーザー i にフォローされているユーザーの集合を B _ i とする。
    F = [[] for _ in range(N)]
    B = [[] for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            F[a].append(b)
            B[b].append(a)
        elif t == 2:
            if a in F[b]:
                F[b].remove(a)
                B[a].remove(b)
        else:
            if a in B[b]:
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()