def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input())))
    #print(A)
    #一番左上のマスからスタート
    x = 0
    y = 0
    ans = []
    ans.append(A[x][y])
    for i in range(N - 1):
        #print("i = " + str(i))
        #print("x = " + str(x))
        #print("y = " + str(y))
        #print("ans = " + str(ans))
        if x == 0:
            if y == 0:
                if A[x + 1][y] >= A[x][y + 1]:
                    x += 1
                else:
                    y += 1
            elif y == N - 1:
                if A[x + 1][y] >= A[x][y - 1]:
                    x += 1
                else:
                    y -= 1
            else:
                if A[x + 1][y] >= A[x][y - 1] and A[x + 1][y] >= A[x][y + 1]:
                    x += 1
                elif A[x][y - 1] >= A[x + 1][y] and A[x][y - 1] >= A[x][y + 1]:
                    y -= 1
                else:
                    y += 1
        elif x == N - 1:
            if y == 0:
                if A[x - 1][y] >= A[x][y + 1]:
                    x -= 1
                else:
                    y += 1
            elif y == N - 1:
                if A[x - 1][y] >= A[x][y - 1]:
                    x -= 1
                else:
                    y -= 1
            else:
                if A[x - 1][y] >= A[x][y - 1] and A[x - 1][y] >= A[x][y + 1]:
                    x -= 1
                elif A[x][y - 1] >= A[x - 1][y] and A[x][y - 1] >= A[x][y + 1]:
                    y -= 1
                else:
