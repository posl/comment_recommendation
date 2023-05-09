def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N-5):
        for j in range(N-5):
            # 横方向
            if S[i][j:j+6] == "######":
                print("Yes")
                return
            # 縦方向
            if all(S[i+k][j] == "#" for k in range(6)):
                print("Yes")
                return
            # 右下方向
            if all(S[i+k][j+k] == "#" for k in range(6)):
                print("Yes")
                return
            # 左下方向
            if all(S[i+k][j-k] == "#" for k in range(6)):
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()