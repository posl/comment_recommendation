def main():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] == T[i]:
            print("Yes")
        else:
            print("No")
