def main():
    # H_1 W_1
    # A_{1, 1} A_{1, 2} ...A_{1, W_1}
    # A_{2, 1} A_{2, 2} ...A_{2, W_1}
    # .
    # .
    # .
    # A_{H_1, 1} A_{H_1, 2} ...A_{H_1, W_1}.
    # H_2 W_2
    # B_{1, 1} B_{1, 2} ...B_{1, W_2}
    # B_{2, 1} B_{2, 2} ...B_{2, W_2}
    # .
    # .
    # .
    # B_{H_2, 1} B_{H_2, 2} ...B_{H_2, W_2}
    h_1, w_1 = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h_1)]
    h_2, w_2 = map(int, input().split())
    b = [list(map(int, input().split())) for i in range(h_2)]
    for i in range(h_1 - h_2 + 1):
        for j in range(w_1 - w_2 + 1):
            if a[i][j] == b[0][0]:
                flag = True
                for k in range(h_2):
                    for l in range(w_2):
                        if a[i + k][j + l] != b[k][l]:
                            flag = False
                if flag:
                    print("Yes")
                    return
    print("No")
    return
