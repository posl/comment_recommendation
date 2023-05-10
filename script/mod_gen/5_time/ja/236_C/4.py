def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    #print(N, M)
    #print(S)
    #print(T)
    #print(S[0])
    #print(T[0])
    #print(S[N-1])
    #print(T[M-1])
    if S[0] == T[0] and S[N-1] == T[M-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()