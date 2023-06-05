def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]
    #print(N, X)
    #print(AB)
    #print(A)
    #print(B)
    #print(sum(A))
    #print(sum(B))
    #print(X)
    #print(X*sum(A))
    #print(X*sum(B))
    #print(sum(A)+sum(B))
    #print(sum(A)+sum(B)+X)
    #print(X*sum(A)+X*sum(B))
    #print(X*sum(A)+X*sum(B)+sum(A)+sum(B))
    print(X*sum(A)+X*sum(B)+sum(A)+sum(B))
    return

if __name__ == '__main__':
    main()