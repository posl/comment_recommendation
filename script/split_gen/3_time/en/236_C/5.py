def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    ans = [0] * N
    for i in range(N):
        if S[i] in T:
            ans[i] = 1
    for i in range(N):
        if ans[i] == 1:
            print("Yes")
        else:
            print("No")
