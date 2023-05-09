def main():
    N = int(input())
    A = []
    for i in range(N):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            B = sorted([a for a in A if a <= query[1]])
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[-query[2]])
        elif query[0] == 3:
            B = sorted([a for a in A if a >= query[1]])
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[query[2]-1])

if __name__ == '__main__':
    main()