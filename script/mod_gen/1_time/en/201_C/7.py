def main():
    S = input()
    S = S.replace("?", "o")
    n = 0
    for i in range(10):
        if S[i] == "o":
            n += 1
    print(10 ** (4 - n))

if __name__ == '__main__':
    main()