def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #print(N, A, B, P, Q, R, S)
    #print()
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (A <= i <= N-B+1 and A <= j <= N-B+1 and i+j == A+B) or (A <= i <= N-B+1 and B <= j <= N-A+1 and i-j == A-B):
                print('#', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    main()