def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    x = 0
    for i in range(N):
        x += A[i] / B[i]
    x /= 2
    y = 0
    for i in range(N):
        y += A[i] / B[i]
        if y >= x:
            print(x)
            return
    print(x)
main()

if __name__ == '__main__':
    main()