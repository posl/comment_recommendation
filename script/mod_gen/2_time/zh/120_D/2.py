def main():
    N, M = map(int, input().split())
    print(N, M)
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    print("hello world")

if __name__ == '__main__':
    main()