def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input()
    input_line = input_line.split(" ")
    N = int(input_line[0])
    P = int(input_line[1])
    Q = int(input_line[2])
    R = int(input_line[3])
    S = int(input_line[4])
    input_line = input()
    input_line = input_line.split(" ")
    A = []
    for i in range(N):
        A.append(int(input_line[i]))
    # print(N, P, Q, R, S)
    # print(A)
    B = []
    for i in range(N):
        if i >= P-1 and i <= Q-1:
            B.append(A[i+R-Q])
        elif i >= R-1 and i <= S-1:
            B.append(A[i+P-R])
        else:
            B.append(A[i])
    # print(B)
    for i in range(N):
        if i == N-1:
            print(B[i])
        else:
            print(B[i], end="")
