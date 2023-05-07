def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            P += max(0, A[i-1] - A[i])
    print(P)

if __name__ == '__main__':
    main()