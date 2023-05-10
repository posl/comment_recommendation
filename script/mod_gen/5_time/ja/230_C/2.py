def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1つ目の操作
    k = min(N-A, N-B)
    for i in range(max(1-A, 1-B), k+1):
        if P <= A+i <= Q and R <= B+i <= S:
            print("#", end="")
        else:
            print(".", end="")
    print()
    # 2つ目の操作
    k = min(N-A, B-1)
    for i in range(max(1-A, B-N), k+1):
        if P <= A+i <= Q and R <= B-i <= S:
            print("#", end="")
        else:
            print(".", end="")
    print()

if __name__ == '__main__':
    main()