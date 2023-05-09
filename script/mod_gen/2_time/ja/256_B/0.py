def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    B = [0, 0, 0, 0]
    for i in range(N):
        B[0] += 1
        for j in range(4):
            if B[j] > 0:
                B[j] -= 1
                if j + A[i] < 4:
                    B[j + A[i]] += 1
                else:
                    P += 1
    print(P)

if __name__ == '__main__':
    main()