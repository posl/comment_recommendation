def main():
    S = input()
    if len(S) != 4:
        print("No")
        return
    for s in S:
        if S.count(s) != 2:
            print("No")
            return
    print("Yes")
