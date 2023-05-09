def main():
    N, M = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(M)]
    ABs.sort()
    d = {}
    for AB in ABs:
        A = AB[0]
        B = AB[1]
        if A not in d:
            d[A] = [B]
        else:
            d[A].append(B)
        if B not in d:
            d[B] = [A]
        else:
            d[B].append(A)
    for i in range(1, N+1):
        if i not in d:
            print(0)
        else:
            print(len(d[i])+1, end=" ")
            for j in sorted(d[i]):
                print(j, end=" ")
            print()

if __name__ == '__main__':
    main()