def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    if S[0] == T[0] and S[N-1] == T[M-1]:
        print("Yes")
    else:
        print("No")
