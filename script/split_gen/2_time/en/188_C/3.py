def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(a, i) for i, a in enumerate(A)]
    A.sort()
    A = [a[1] for a in A]
    for i in range(N):
        A = [min(a, b) for a, b in zip(A[::2], A[1::2])]
    print(A[0] + 1)
