def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P = 0
        else:
            P = P + A[i-1] - 1
    print(P)

if __name__ == '__main__':
    main()