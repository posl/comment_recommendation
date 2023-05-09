def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    S = list(set(S))
    T = list(set(T))
    if len(S) == len(T):
        print("Yes")
    else:
        print("No")
