def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0 for i in range(M+1)]
    for i in range(M+1):
        b[i] = c[i] // a[0]
    for i in range(M+1):
        for j in range(N+1):
            c[i+j] -= b[i] * a[j]
    print(" ".join(map(str, b)))

if __name__ == '__main__':
    main()