def main():
    N, Q = map(int, input().split())
    users = [0] * N
    for i in range(Q):
        T, A, B = map(int, input().split())
        if T == 1:
            users[A - 1] |= 1 << (B - 1)
        elif T == 2:
            users[A - 1] &= ~(1 << (B - 1))
        else:
            print("Yes" if users[A - 1] & (1 << (B - 1)) and users[B - 1] & (1 << (A - 1)) else "No")

if __name__ == '__main__':
    main()