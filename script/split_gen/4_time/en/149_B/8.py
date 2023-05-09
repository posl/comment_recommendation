def main():
    #input
    A, B, K = map(int, input().split())
    #compute
    if A >= K:
        A -= K
    else:
        K -= A
        A = 0
        if B >= K:
            B -= K
        else:
            B = 0
    #output
    print(A, B)
