def main():
    S = input()
    l = len(S)
    n = 0
    for i in range(l):
        n = n*26 + ord(S[i]) - 64
    print(n)

if __name__ == '__main__':
    main()