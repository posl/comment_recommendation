def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1行目
    for i in range(R, S+1):
        if P <= A + B - i <= Q:
            print("#", end="")
        else:
            print(".", end="")
    print()
    # 2行目以降
    for i in range(P+1, Q+1):
        if i < A + B - S:
            print(".", end="")
        elif i <= A + B - R:
            print("#", end="")
        else:
            print(".", end="")
        if i < A - B + R:
            print("." * (S - R), end="")
        elif i <= A - B + S:
            print("#" * (S - R), end="")
        else:
            print("." * (S - R), end="")
        print()
