def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    if N == 1:
        print(A[0])
    else:
        for i in range(4*N-1):
            if A[i] != A[i+1]:
                print(A[i])
                break
