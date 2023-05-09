def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    count = 1
    for i in range(N):
        if X == A[X - 1]:
            break
        X = A[X - 1]
        count += 1
    print(count)
