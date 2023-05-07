def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    if A > B:
        A = N + 1 - A
        B = N + 1 - B
        P = N + 1 - P
        Q = N + 1 - Q
    if A + B - 1 < P:
        for i in range(Q - P + 1):
            print('.' * (S - R + 1))
        return
    if N - A + 1 < R:
        for i in range(Q - P + 1):
            print('.' * (S - R + 1))
        return
    if A + B - 1 > Q:
        for i in range(Q - P + 1):
            print('#' * (S - R + 1))
        return
    if N - A + 1 > S:
        for i in range(Q - P + 1):
            print('#' * (S - R + 1))
        return
    if A + B - 1 >= P and A + B - 1 <= Q:
        print('.' * (A + B - 1 - P) + '#' * (Q - A - B + 2) + '.' * (S - R + 1))
        P = A + B
    if N - A + 1 >= R and N - A + 1 <= S:
        print('.' * (S - R + 1) + '#' * (N - A + 1 - R + 1) + '.' * (N - A))
        S = N - A
    for i in range(P - A - B + 1, Q - A - B + 1):
        if i < 0:
            print('.' * (S - R + 1))
        elif i == 0:
            print('.' * (S - R + 1))
        elif i == 1:
            print('.' * (S - R + 1))
        else:
            print('.' * (S - R + 1))

if __name__ == '__main__':
    main()