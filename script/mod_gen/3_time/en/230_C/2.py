def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if ((i+j) % 2 == 0) and (A <= i <= N-B+1) and (B <= j <= N-A+1):
                print('#', end='')
            elif ((i+j) % 2 == 1) and (A <= i <= N-B+1) and (B <= j <= N-A+1):
                print('.', end='')
            elif ((i+j) % 2 == 0) and (A <= i <= N-B+1) and (B-1 <= j <= N-A):
                print('#', end='')
            elif ((i+j) % 2 == 1) and (A <= i <= N-B+1) and (B-1 <= j <= N-A):
                print('.', end='')
            elif ((i+j) % 2 == 0) and (A-1 <= i <= N-B) and (B <= j <= N-A+1):
                print('#', end='')
            elif ((i+j) % 2 == 1) and (A-1 <= i <= N-B) and (B <= j <= N-A+1):
                print('.', end='')
            elif ((i+j) % 2 == 0) and (A-1 <= i <= N-B) and (B-1 <= j <= N-A):
                print('#', end='')
            elif ((i+j) % 2 == 1) and (A-1 <= i <= N-B) and (B-1 <= j <= N-A):
                print('.', end='')
        print()

if __name__ == '__main__':
    main()