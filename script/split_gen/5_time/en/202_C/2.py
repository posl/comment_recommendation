def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    count = 0
    for i in range(n):
        a = A[i]
        b = B[i]
        c = C[i]
        count += B.index(a) * (n - C.index(a))
    print(count)
