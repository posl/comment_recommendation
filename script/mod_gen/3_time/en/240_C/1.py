def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort(reverse=True)
    if X < A[0] or X > B[0]:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()