def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a,b = map(int,input().split())
        S.append([a,b])
    for i in range(N):
        c,d = map(int,input().split())
        T.append([c,d])
    S.sort()
    T.sort()
    for i in range(N):
        S[i][0] -= T[0][0]
        S[i][1] -= T[0][1]
    T[0][0] = 0
    T[0][1] = 0
    #print(S)
    #print(T)
    for i in range(N):
        if S[i][0] != 0:
            p = S[i][0]
            break
    else:
        for i in range(N):
            if S[i][1] != 0:
                p = S[i][1]
                break
        else:
            print("Yes")
            exit()
    #print(p)
    for i in range(N):
        if S[i][0] % p != 0 or S[i][1] % p != 0:
            print("No")
            exit()
    for i in range(N):
        S[i][0] //= p
        S[i][1] //= p
    for i in range(N):
        S[i][0] -= T[0][0]
        S[i][1] -= T[0][1]
    T[0][0] = 0
    T[0][1] = 0
    #print(S)
    #print(T)
    for i in range(N):
        if S[i][0] != 0:
            q = S[i][0]
            break
    else:
        for i in range(N):
            if S[i][1] != 0:
                q = S[i][1]
                break
        else:
            print("Yes")
            exit()
    #print(q)
    for i in range(N):
        if S[i][0] % q != 0 or S[i][1] % q != 0:
            print("No")
            exit()
    for i in range(N):
        S[i][0] //= q
        S[i][1] //= q
    for i in range(N):
        S[i][0] -= T[

if __name__ == '__main__':
    main()