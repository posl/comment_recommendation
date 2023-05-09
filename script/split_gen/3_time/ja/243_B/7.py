def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = {}
    b = {}
    c = 0
    d = 0
    for i in range(N):
        a[A[i]] = i
        b[B[i]] = i
    for i in range(N):
        if A[i] in b:
            d += 1
            if a[A[i]] == b[A[i]]:
                c += 1
    print(c)
    print(d - c)
