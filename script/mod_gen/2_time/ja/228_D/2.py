def main():
    Q = int(input())
    A = [-1] * 1048576
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % 1048576] != -1:
                h += 1
            A[h % 1048576] = x
        else:
            print(A[x % 1048576])

if __name__ == '__main__':
    main()