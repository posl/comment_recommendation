def main():
    k = int(input())
    s = input()
    t = input()
    s = s[:4]
    t = t[:4]
    s = [int(i) for i in s]
    t = [int(i) for i in t]
    s.sort(reverse=True)
    t.sort(reverse=True)
    s = ''.join([str(i) for i in s])
    t = ''.join([str(i) for i in t])
    s = int(s)
    t = int(t)
    s = s * (10**5) + 10**4
    t = t * (10**5) + 10**4
    print(s)
    print(t)
    # print(s)
    # print(t)
    # s = [int(i) for i in s]
    # t = [int(i) for i in t]
    # s.sort(reverse=True)
    # t.sort(reverse=True)
    # print(s)
    # print(t)
    # s = ''.join([str(i) for i in s])
    # t = ''.join([str(i) for i in t])
    # s = int(s)
    # t = int(t)
    # print(s)
    # print(t)
    # print(s > t)
    # print(s == t)
    # print(s < t)
    # print(s * 10)
    # print(s * 10 + 9)
    # print(s * 10 + 10)
    # print(s * 10 + 11)
    # print(s * 10 + 12)
    # print(s * 10 + 13)
    # print(s * 10 + 14)
    # print(s * 10 + 15)
    # print(s * 10 + 16)
    # print(s * 10 + 17)
    # print(s * 10 + 18)
    # print(s * 10 + 19)
    # print(s * 10 + 20)
    # print(s * 10 + 21)
    # print(s * 10 + 22)
    # print(s * 10 + 23)
    # print(s * 10 + 24)
    # print(s * 10 + 25)
    # print(s * 10 + 26)
    # print(s * 10 + 27)

if __name__ == '__main__':
    main()