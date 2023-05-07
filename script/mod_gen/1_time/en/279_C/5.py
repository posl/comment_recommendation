def main():
    H,W = map(int,input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    S = sorted(S)
    T = sorted(T)
    flag = True
    for i in range(H):
        if S[i] != T[i]:
            flag = False
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()