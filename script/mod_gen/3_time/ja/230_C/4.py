def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #print(N, A, B)
    #print(P, Q, R, S)
    for i in range(P, Q+1):
        for j in range(R, S+1):
            ans = 0
            if i >= A and j >= B:
                ans += min(N-i+1, N-j+1)
            if i >= A and j <= B:
                ans += min(N-i+1, j)
            if i <= A and j >= B:
                ans += min(i, N-j+1)
            if i <= A and j <= B:
                ans += min(i, j)
            if ans % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()

if __name__ == '__main__':
    main()