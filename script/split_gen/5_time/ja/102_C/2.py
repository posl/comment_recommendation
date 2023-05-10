def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    b = A[N//2]
    total = 0
    for i in range(N):
        total += abs(A[i] - (b+i+1))
    print(total)
