def main():
    N = int(input())
    A = []
    B = []
    for i in range(N-1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)

if __name__ == '__main__':
    main()