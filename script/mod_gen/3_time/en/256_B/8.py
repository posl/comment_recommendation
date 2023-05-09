def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            if A[i] == 1:
                P += 1
            elif A[i] == 2:
                P += 2
            elif A[i] == 3:
                P += 1
            elif A[i] == 4:
                P += 2
    print(P)

if __name__ == '__main__':
    main()