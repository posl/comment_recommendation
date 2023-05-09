def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) != N or len(set(T)) != N:
        print("No")
    else:
        for i in range(N):
            for j in range(i+1, N):
                if S[i] == T[j] and S[j] == T[i]:
                    print("No")
                    exit()
        print("Yes")

if __name__ == '__main__':
    main()