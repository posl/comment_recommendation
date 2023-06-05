def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != A[1]:
        print(A[0])
    elif A[-1] != A[-2]:
        print(A[-1])
    else:
        for i in range(1, 4*N-1):
            if A[i] != A[i-1] and A[i] != A[i+1]:
                print(A[i])
                break
