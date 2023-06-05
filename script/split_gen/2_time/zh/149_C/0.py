def main():
    #input
    A, B, K = map(int, input().split())
    #calc
    if A >= K:
        A = A - K
    elif A < K:
        B = B - (K - A)
        A = 0
        if B < 0:
            B = 0
    #output
    print(A, B)
