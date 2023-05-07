def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    #print(S)
    #print(T)
    for i in range(N-1):
        for j in range(i+1, N):
            if T[i] == T[j]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()