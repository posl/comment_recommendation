def main():
    n = int(input())
    # n = 576461302059761664
    n = bin(n)[2:]
    n = list(n)
    n.reverse()
    # print(n)
    # print(len(n))
    l = len(n)
    # print(l)
    ans = []
    for i in range(l):
        if n[i] == '1':
            ans.append(2**i)
    # print(ans)
    # print(len(ans))
    # print(2**60)
    # print(2**60>576461302059761664)
    # print(2**60>5764

if __name__ == '__main__':
    main()