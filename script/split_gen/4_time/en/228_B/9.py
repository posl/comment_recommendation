def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(X)
    A.sort()
    count = 1
    for i in range(1, N):
        if A[i-1] != A[i]:
            count += 1
    print(count)
