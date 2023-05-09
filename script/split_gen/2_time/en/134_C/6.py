def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    a = max(A)
    b = A.index(a)
    A[b] = 0
    c = max(A)
    for i in range(N):
        if i != b:
            print(c)
        else:
            print(a)
main()
