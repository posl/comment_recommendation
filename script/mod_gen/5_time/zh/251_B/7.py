def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] > W:
        print(0)
    else:
        if N == 1:
            if A[0] <= W:
                print(1)
            else:
                print(0)
        elif N == 2:
            if A[0] + A[1] <= W:
                print(3)
            else:
                if A[0] <= W:
                    print(2)
                else:
                    print(1)
        else:
            if A[0] + A[1] + A[2] <= W:
                print((N * (N - 1) * (N - 2) // 6) * 7)
            else:
                if A[0] + A[1] <= W:
                    print((N * (N - 1) // 2) * 3 - 2)
                else:
                    if A[0] <= W:
                        print((N - 1) * 2 - 1)
                    else:
                        print(1)
main()
