def main():
    s = input()
    k = int(input())
    if len(s) == 1:
        print(0)
        return
    if k == 0:
        print(max([len(i) for i in s.split("X")]))
        return
    if "X" not in s:
        print(len(s))
        return
    s = s.replace("X", "X.")
    s = s.replace(".", ".X")
    s = s[1:-1]
    s = s.split(".")
    if len(s) == 1:
        print(len(s[0]))
        return
    if s[0] == "":
        s = s[1:]
    if s[-1] == "":
        s = s[:-1]
    if len(s) == 1:
        print(len(s[0]))
        return
    if len(s) == 2:
        print(max([len(s[0]), len(s[1])]))
        return
    if len(s) == 3:
        print(max([len(s[0]), len(s[1]), len(s[2])]))
        return
    if len(s) == 4:
        print(max([len(s[0]), len(s[1]), len(s[2]), len(s[3])]))
        return
    if len(s) == 5:
        print(max([len(s[0]), len(s[1]), len(s[2]), len(s[3]), len(s[4])]))
        return

if __name__ == '__main__':
    main()