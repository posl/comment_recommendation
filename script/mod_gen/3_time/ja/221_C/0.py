def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    a = 0
    b = 0
    for i in range(len(N)):
        if i % 2 == 0:
            a = a * 10 + int(N[i])
        else:
            b = b * 10 + int(N[i])
    print(a * b)

if __name__ == '__main__':
    main()