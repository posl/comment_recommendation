def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #print(A)
    B = []
    for i in range(N):
        B.append(tuple(A[i][1:]))
    #print(B)
    ans = len(set(B))
    print(ans)
main()

if __name__ == '__main__':
    main()