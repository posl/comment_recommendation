def main():
    n = input()
    # n = 998244353
    n = list(n)
    n = list(map(int, n))
    n.sort()
    n.reverse()
    # print(n)
    a = n[0]
    b = n[1]
    for i in range(2, len(n)):
        if a > b:
            b = b * 10 + n[i]
        else:
            a = a * 10 + n[i]
    print(a * b)

if __name__ == '__main__':
    main()