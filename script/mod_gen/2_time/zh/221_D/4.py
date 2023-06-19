def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    # print("")
    # for i in range(n):
    #     print(str(a[i]) + " " + str(b[i]))
    # print("")
    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))
    # print("")
    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))
    # print("")
    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))
    # print("")
    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))
    # print("")
    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))
    # print("")
    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))
    # print("")
    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))
    # print("")
    # for i in range(n):
    #     print(str(a[i] + b[i] - 1) + " " + str(a[i] - 1))
    # print("")
    l = []
    for i in range(n):
        l.append([a[i] + b[i] - 1, a[i] - 1])
    # print(l)
    # print("")
    l.sort()
    # print(l)
    # print("")
    # for i in range(n):
    #     print(str(l[i][0]) + " " + str(l[i

if __name__ == '__main__':
    main()