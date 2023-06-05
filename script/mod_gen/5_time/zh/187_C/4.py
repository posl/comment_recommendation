def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s_set = set(s)
    for i in s_set:
        if i[0] == "!":
            if i[1:] in s_set:
                print(i[1:])
                return
        else:
            if "!"+i in s_set:
                print(i)
                return
    print("satisfiable")

if __name__ == '__main__':
    main()