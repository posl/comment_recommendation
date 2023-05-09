def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    P = 0
    for i in range(N):
        if i == 0:
            P = 0
        else:
            P = P + A[i-1]
            if P >= 4:
                P = P - 4
    print(P)

if __name__ == '__main__':
    main()