def main():
    N,M = map(int,input().split())
    fri = [[] for i in range(N+1)]
    for i in range(M):
        A,B = map(int,input().split())
        fri[A].append(B)
        fri[B].append(A)
    ans = 0
    for i in range(1,N+1):
        if fri[i] != []:
            ans += 1
            for j in fri[i]:
                fri[j] = []
    print(ans)
main()

if __name__ == '__main__':
    main()