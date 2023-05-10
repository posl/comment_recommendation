def main():
    # Get input
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    
    # Initialize variables
    ans = 0
    w = 0
    wsum = sum(W)
    for i in range(N):
        if S[i] == '0':
            w += W[i]
        else:
            ans = max(ans, wsum-w)
    print(ans)
