def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_even = -1
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] + A[j]) % 2 == 0:
                if A[i] + A[j] > max_even:
                    max_even = A[i] + A[j]
                break
    print(max_even)
