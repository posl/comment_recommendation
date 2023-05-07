def main():
    S = input()
    T = input()
    S = S.replace("a", "aa")
    S = S.replace("b", "bb")
    S = S.replace("c", "cc")
    if S == T:
        print("Yes")
    else:
        print("No")
