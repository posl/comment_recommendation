def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] != X:
            count += 1
            X = A[i]
    print(count)
