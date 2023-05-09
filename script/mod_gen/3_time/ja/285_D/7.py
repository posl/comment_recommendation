def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) == N and len(set(T)) == N:
        for i in range(N):
            if S[i] == T[i]:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()