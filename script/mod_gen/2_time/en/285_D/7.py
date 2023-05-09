def solve():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    S_set = set(S)
    T_set = set(T)
    if len(S_set) == len(S) and len(T_set) == len(T) and len(S_set & T_set) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()