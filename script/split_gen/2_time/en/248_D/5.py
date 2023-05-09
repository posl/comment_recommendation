def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    counter = [0] * N
    for a in A:
        counter[a - 1] += 1
    for l, r, x in queries:
        print(counter[x - 1] - (A[l - 1] != x) - (A[r - 1] != x))
