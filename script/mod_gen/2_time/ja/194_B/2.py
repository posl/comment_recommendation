def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    print(min(A[0]+B[0], max(A[0], B[1]), max(A[1], B[0])))

if __name__ == '__main__':
    main()