def main():
    H_1, W_1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H_1)]
    H_2, W_2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H_2)]
    if H_1 > H_2 and W_1 > W_2:
        for i in range(H_1 - H_2 + 1):
            for j in range(W_1 - W_2 + 1):
                if A[i][j] == B[0][0]:
                    for k in range(H_2):
                        for l in range(W_2):
                            if A[i + k][j + l] != B[k][l]:
                                break
                        else:
                            continue
                        break
                    else:
                        print("Yes")
                        return
        print("No")
        return
    print("No")

if __name__ == '__main__':
    main()