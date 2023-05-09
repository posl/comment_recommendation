def main():
    A, B, N = map(int, input().split())
    if A >= B:
        print(B-1)
        return
    if N >= B-1:
        print(A*(B-1)//B)
        return
    print(A*N//B)
