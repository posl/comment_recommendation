def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    max_even = -1
    for i in range(N-1):
        if A[i] == A[i+1]:
            max_even = A[i]
    print(max_even)
