def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    result = 1000000000
    i = 0
    for b in B:
        while i < N and A[i] < b:
            i += 1
        if i == 0:
            result = min(result, abs(A[i] - b))
        elif i == N:
            result = min(result, abs(A[i - 1] - b))
        else:
            result = min(result, abs(A[i - 1] - b), abs(A[i] - b))
    print(result)
