def main():
    n,m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    min_diff = 1000000000
    for i in range(n):
        diff = abs(A[i] - B[0])
        if diff < min_diff:
            min_diff = diff
        for j in range(m):
            diff = abs(A[i] - B[j])
            if diff < min_diff:
                min_diff = diff
            else:
                break
    print(min_diff)
