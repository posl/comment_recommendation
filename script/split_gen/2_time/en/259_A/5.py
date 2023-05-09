def main():
    #input
    N, M, X, T, D = map(int, input().split())
    #compute
    if M < X:
        ans = T + (N - X) * D
    else:
        ans = T + (M - X) * D + (N - M) * D
    #output
    print(ans)
