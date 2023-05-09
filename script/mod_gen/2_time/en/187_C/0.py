def main():
    n = int(input())
    s = set()
    for i in range(n):
        si = input()
        if si[0] == "!":
            if si[1:] in s:
                print(si[1:])
                return
            else:
                s.add(si)
        else:
            if "!" + si in s:
                print(si)
                return
            else:
                s.add(si)
    print("satisfiable")

if __name__ == '__main__':
    main()