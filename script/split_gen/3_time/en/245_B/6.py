def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A)
    if A[0] > 0:
        print(0)
        return
    for i in range(N-1):
        if A[i+1] - A[i] > 1:
            print(A[i]+1)
            return
    print(A[-1]+1)
    return
