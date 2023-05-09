def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i <= A + B - j <= N) or (i >= A + B - j >= N+1):
                print('#', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    main()