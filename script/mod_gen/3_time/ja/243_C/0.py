def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'R' and X[i] > Y[i]:
            print('Yes')
            return
        if S[i] == 'L' and X[i] < Y[i]:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()