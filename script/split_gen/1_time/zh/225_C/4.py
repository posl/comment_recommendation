def main():
    N, M = map(int, input().split())
    B = []
    for i in range(N):
        B.append(list(map(int, input().split())))
    if N == 1 and M == 1:
        if B[0][0] == 1:
            print("Yes")
        else:
            print("No")
        return
    if N == 1:
        for i in range(1, M):
            if B[0][i] - B[0][i-1] != 1:
                print("No")
                return
        print("Yes")
        return
    if M == 1:
        for i in range(1, N):
            if B[i][0] - B[i-1][0] != 7:
                print("No")
                return
        print("Yes")
        return
    for i in range(N):
        for j in range(M):
            if B[i][j] == 1:
                if i == 0 or j == 0:
                    print("No")
                    return
                if B[i][j-1] != 7*(i+1)+j-1:
                    print("No")
                    return
                if B[i-1][j] != 7*i+j-6:
                    print("No")
                    return
                for k in range(i+1, N):
                    if B[k][j] - B[k-1][j] != 7:
                        print("No")
                        return
                for k in range(j+1, M):
                    if B[i][k] - B[i][k-1] != 1:
                        print("No")
                        return
                print("Yes")
                return
    print("No")
