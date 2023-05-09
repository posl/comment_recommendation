def main():
    S = input()
    if S[0] == "0":
        print("No")
        return
    # 1 が立っている列の間に 0 が存在するかどうか
    for i in range(1, 9):
        if S[i] == "1" and S[i+1] == "0":
            print("No")
            return
    print("Yes")
