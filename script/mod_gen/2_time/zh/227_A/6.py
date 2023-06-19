def main():
    n,k,a = map(int,input().split())
    # n,k,a = map(int, "3 3 2".split())
    # n,k,a = map(int, "1 100 1".split())
    # n,k,a = map(int, "3 14 2".split())
    # print(n,k,a)
    # print(type(n),type(k),type(a))
    # for i in range(1,k+1):
    #     print("i:",i)
    #     if a < n:
    #         a += 1
    #     else:
    #         a = 1
    #     print("a:",a)
    # print(a)
    # for i in range(1,k+1):
    #     print("i:",i)
    #     a = (a + 1) if a < n else 1
    #     print("a:",a)
    # print(a)
    # print((a + k - 1) % n)
    # print(a + k - 1)
    # print((a + k - 1) % n)
    # print(((a + k - 1) % n) + 1)
    print((a + k - 1) % n + 1)

if __name__ == '__main__':
    main()