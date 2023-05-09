def main():
    #input
    N, M, X, T, D = map(int, input().split())
    #compute
    if M >= X:
        h = T + D*(M-X)
    else:
        h = T
    #output
    print(h)
