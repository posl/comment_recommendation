def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i
    p = 0
    for i in range(N):
        if Q[i] > p:
            p = Q[i]
        else:
            print(i + 1, end = " ")
    print(N)

if __name__ == '__main__':
    main()