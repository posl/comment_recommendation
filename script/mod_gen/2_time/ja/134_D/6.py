def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = []
    for i in range(N):
        if A[i] == 1:
            B.append(i+1)
    if len(B)%2 == 0:
        print(len(B))
        for i in range(len(B)):
            print(B[i])
    else:
        print(-1)

if __name__ == '__main__':
    main()