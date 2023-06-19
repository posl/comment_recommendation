def main():
    s = input()
    if len(s) % 2 == 1:
        print("No")
        return
    for i in range(0, len(s), 2):
        if s[i] not in "RL":
            print("No")
            return
    for i in range(1, len(s), 2):
        if s[i] not in "UD":
            print("No")
            return
    print("Yes")
main()
