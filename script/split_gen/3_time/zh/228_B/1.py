def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A[X-1] = 0
    A.sort()
    A = A[::-1]
    count = 0
    for i in range(N):
        if A[i] != 0:
            count += 1
        else:
            break
    print(count)
