def main():
    s = input()
    l = len(s)
    if l%2 != 0:
        print("否")
        return
    for i in range(l):
        if s[i] == "(":
            continue
        elif s[i] == ")":
            continue
        else:
            print("否")
            return
    print("是")
    return
