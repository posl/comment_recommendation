def main():
    S = input()
    if S[0] != "(" or S[-1] != ")":
        print("No")
        return
    cnt = 0
    for s in S:
        if s == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print("No")
            return
    if cnt != 0:
        print("No")
        return
    print("Yes")
    return
