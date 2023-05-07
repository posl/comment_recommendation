def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    B = []
    for i in range(N):
        if A[i] == 0:
            continue
        else:
            B.append(A[i])
    B.sort()
    for i in range(M):
        if len(B) == 0:
            break
        else:
            B[0] = B[0] // 2
            if B[0] == 0:
                del B[0]
            else:
                B.sort()
    print(sum(B))

if __name__ == '__main__':
    main()