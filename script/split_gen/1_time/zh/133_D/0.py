def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    total = sum(A)
    for i in range(N):
        print(total - A[i], end=' ')
    print()
