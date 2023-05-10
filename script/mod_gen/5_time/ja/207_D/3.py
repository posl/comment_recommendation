def solve():
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
    if S == T:
        print("Yes")
        exit()
    for i in range(N):
        S.sort()
        T.sort()
        if S == T:
            print("Yes")
            exit()
        S = rotate(S)
    print("No")

if __name__ == '__main__':
    solve()