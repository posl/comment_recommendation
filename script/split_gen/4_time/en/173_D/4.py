def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    total = 0
    for i in range(N - 1):
        total += A[i]
    print(total)
