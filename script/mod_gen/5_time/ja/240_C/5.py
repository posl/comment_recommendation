def main():
    N, X = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    pos = 0
    for i in range(N):
        pos += a[i]
        if pos > X:
            print("No")
            return
        pos += b[i]
    if pos == X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()