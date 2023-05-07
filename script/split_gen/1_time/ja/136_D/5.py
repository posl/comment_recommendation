def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[N-1] = 1
    for i in range(1,N-1):
        if S[i-1] == "R":
            ans[i] += 1
        else:
            ans[i-1] += 1
    for i in range(N):
        print(ans[i],end=" ")
