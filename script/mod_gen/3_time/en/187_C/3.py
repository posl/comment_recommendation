def main():
    n = int(input())
    s = [input() for i in range(n)]
    s1 = []
    s2 = []
    for i in s:
        if i[0] == "!":
            s1.append(i[1:])
        else:
            s2.append(i)
    s1 = set(s1)
    s2 = set(s2)
    s3 = s1 & s2
    if len(s3) == 0:
        print("satisfiable")
    else:
        print(s3.pop())

if __name__ == '__main__':
    main()