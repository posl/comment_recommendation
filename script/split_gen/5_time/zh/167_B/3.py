def main():
    A, B, C, K = map(int, input().split())
    #print(A, B, C, K)
    if A >= K:
        print(K)
    elif A + B >= K:
        print(A)
    else:
        print(A - (K - A - B))
