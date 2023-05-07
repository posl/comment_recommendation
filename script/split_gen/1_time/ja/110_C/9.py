def main():
    S = input()
    T = input()
    # ソートした結果が一致するかどうかで判定
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")
