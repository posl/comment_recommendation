def main():
    # H_1 W_1
    # A_{1, 1} A_{1, 2} ... A_{1, W_1}
    # A_{2, 1} A_{2, 2} ... A_{2, W_1}
    # .
    # .
    # .
    # A_{H_1, 1} A_{H_1, 2} ... A_{H_1, W_1}
    # H_2 W_2
    # B_{1, 1} B_{1, 2} ... B_{1, W_2}
    # B_{2, 1} B_{2, 2} ... B_{2, W_2}
    # .
    # .
    # .
    # B_{H_2, 1} B_{H_2, 2} ... B_{H_2, W_2}
    # H_1 W_1
    # A_{1, 1} A_{1, 2} ... A_{1, W_1}
    # A_{2, 1} A_{2, 2} ... A_{2, W_1}
    # .
    # .
    # .
    # A_{H_1, 1} A_{H_1, 2} ... A_{H_1, W_1}
    H_1, W_1 = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H_1)]
    # H_2 W_2
    # B_{1, 1} B_{1, 2} ... B_{1, W_2}
    # B_{2, 1} B_{2, 2} ... B_{2, W_2}
    # .
    # .
    # .
    # B_{H_2, 1} B_{H_2, 2} ... B_{H_2, W_2}
    H_2, W_2 = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(H_2)]
    # H_1 >= H_2 かつ W_1 >= W_2 でないなら、No
    if

if __name__ == '__main__':
    main()