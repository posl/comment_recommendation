def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P += 1
        else:
            P += A[i-1]
        if P >= 4:
            P -= 4
    print(P)

if __name__ == '__main__':
    main()