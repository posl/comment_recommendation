def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j) % 2 == 0:
                if A <= i <= N-B+1 and A <= j <= N-B+1:
                    print('#', end='')
                elif 1 <= i <= N-A+1 and 1 <= j <= N-A+1:
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                if A <= i <= N-B+1 and 1 <= j <= N-A+1:
                    print('#', end='')
                elif 1 <= i <= N-A+1 and A <= j <= N-B+1:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
