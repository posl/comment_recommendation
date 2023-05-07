def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1 つめの操作で塗られるマスの個数
    c1 = min(N-A, B-1)
    # 2 つめの操作で塗られるマスの個数
    c2 = min(N-A, N-B)
    # 1 つめの操作で塗られるマスの個数
    # 2 つめの操作で塗られるマスの個数
    # のうち、黒く塗られるマスの個数
    c = min(c1, c2)
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if A <= i <= A+c and B-c <= j <= B:
                print("#", end="")
            elif A <= i <= A+c and B <= j <= B+c:
                print("#", end="")
            else:
                print(".", end="")
        print()
