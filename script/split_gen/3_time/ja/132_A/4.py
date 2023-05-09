def main():
    S = input()
    S_set = set(S)
    if len(S_set) == 2:
        for s in S_set:
            if S.count(s) != 2:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")
