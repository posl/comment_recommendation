def main():
    N, A, B = [int(i) for i in input().split()]
    P, Q, R, S = [int(i) for i in input().split()]
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (j-i) % 2 == 0:
                if (A <= i <= N-B+1) and (B <= j <= N-A+1):
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                if (A <= i <= N-B+1) and (B <= j <= N-A+1):
                    print('.', end='')
                else:
                    print('#', end='')
        print()
main()
