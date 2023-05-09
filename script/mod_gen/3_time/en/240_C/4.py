def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(N):
        X -= a[i]
        if X < 0:
            print("No")
            break
        if X == 0:
            print("Yes")
            break
        X -= b[i]
        if X < 0:
            print("No")
            break
        if X == 0:
            print("Yes")
            break
    if X > 0:
        print("No")

if __name__ == '__main__':
    main()