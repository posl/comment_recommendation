def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        ans = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                ans = max(ans,j+1)
        print(ans)
