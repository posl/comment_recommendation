def main():
    N, Q = map(int, input().split())
    A = [0] * N
    for _ in range(Q):
        T, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if T == 1:
            A[a] |= 1 << b
        elif T == 2:
            A[a] &= ~(1 << b)
        else:
            if A[a] & (1 << b):
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()