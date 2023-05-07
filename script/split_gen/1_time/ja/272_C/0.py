def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    if N == 2:
        if A[0] % 2 == 0 or A[1] % 2 == 0:
            print(max(A))
        else:
            print(-1)
    else:
        A.sort()
        if A[-1] % 2 == 0:
            print(A[-1])
        else:
            print(A[-2])
