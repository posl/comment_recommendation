def main():
    h1, w1 = map(int, input().split())
    A = []
    for i in range(h1):
        A.append(list(map(int, input().split())))
    h2, w2 = map(int, input().split())
    B = []
    for i in range(h2):
        B.append(list(map(int, input().split())))
    # print(A, B)
    for i in range(h1-h2+1):
        for j in range(w1-w2+1):
            # print(i, j)
            if A[i][j] == B[0][0]:
                # print(i, j)
                flag = True
                for k in range(h2):
                    for l in range(w2):
                        if A[i+k][j+l] != B[k][l]:
                            flag = False
                            break
                    if not flag:
                        break
                if flag:
                    print("Yes")
                    exit()
    print("No")

if __name__ == '__main__':
    main()