def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    max_total = 0
    for i in range(N):
        total += A[i]
        if total > max_total:
            max_total = total
    print(max_total)
