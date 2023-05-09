def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        if A[i] > 10:
            total += A[i]-10
    print(total)
