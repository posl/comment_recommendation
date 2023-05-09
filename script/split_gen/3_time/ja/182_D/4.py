def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i + 1] += A[i]
    print(max(A) - min(A))
