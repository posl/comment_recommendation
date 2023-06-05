def main():
    N,A,B = map(int,input().split())
    S = input()
    #print(N,A,B)
    #print(S)
    cnt = 0
    for i in range(N):
        if S[i] == S[N-1-i]:
            cnt += 1
    if cnt == N:
        print(A*N+B*(N-1))
    elif cnt == N-1:
        print(A*N+B)
    elif cnt < N-1:
        print(A*N)

if __name__ == '__main__':
    main()