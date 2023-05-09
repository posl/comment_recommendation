def main():
    A,B,K = map(int,input().split())
    if A >= B:
        print(0)
        return
    if K > A:
        print(A)
        return
    print(A-K)
