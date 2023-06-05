def main():
    A,B,K = map(int,input().split())
    if K <= A:
        A -= K
    else:
        K -= A
        A = 0
        if K <= B:
            B -= K
        else:
            B = 0
    print(A,B)
