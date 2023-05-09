def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(N)]
    if N == 1 and M == 1:
        if B[0][0] == 1:
            print("Yes")
        else:
            print("No")
        return
    if N == 1:
        for i in range(M):
            if B[0][i] != i+1:
                print("No")
                return
        print("Yes")
        return
    if M == 1:
        for i in range(N):
            if B[i][0] != i+1:
                print("No")
                return
        print("Yes")
        return
    if N > 10:
        print("No")
        return
    if M > 10:
        print("No")
        return
    A = [[0 for i in range(7)] for j in range(10**2)]
    for i in range(10**2):
        for j in range(7):
            A[i][j] = i*7 + j + 1
    for i in range(N):
        for j in range(M):
            if B[i][j] != A[i][j]:
                print("No")
                return
    print("Yes")
    return
main()
