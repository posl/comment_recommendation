def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j] or T[i] == T[j]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()