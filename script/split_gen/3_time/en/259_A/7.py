def main():
    #input
    N, M, X, T, D = map(int, input().split())
    #compute
    if M < X:
        ans = T + (N-M) * D
    else:
        ans = T + (N-X) * D
    #output
    print(ans)
