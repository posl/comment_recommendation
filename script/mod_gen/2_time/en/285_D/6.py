def solve():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) == len(S) and len(set(T)) == len(T):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()