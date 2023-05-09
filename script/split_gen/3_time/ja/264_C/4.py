def main():
    H_1, W_1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H_1)]
    H_2, W_2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H_2)]
    # どこにも適合しないならNO
    for i in range(H_2):
        for j in range(W_2):
            if B[i][j] not in A[i]:
                print("No")
                exit()
    # 一致するならYES
    for i in range(H_2):
        for j in range(W_2):
            if B[i][j] != A[i][j]:
                print("No")
                exit()
    print("Yes")
