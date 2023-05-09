def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    sum = 0
    for i in range(N):
        sum += a[i] * b[i]
    if sum >= X:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()