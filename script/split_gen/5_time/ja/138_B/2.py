def main():
    N = int(input())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += 1 / A[i]
    print(1 / total)
