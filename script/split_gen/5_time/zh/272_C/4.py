def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_even = -1
    for i in range(N-1):
        for j in range(i+1,N):
            if (A[i]+A[j]) % 2 == 0:
                max_even = max(max_even, A[i]+A[j])
    print(max_even)
