def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    for i in range(4*N-1):
        if A[i] != A[i+1]:
            print(A[i])
            break
