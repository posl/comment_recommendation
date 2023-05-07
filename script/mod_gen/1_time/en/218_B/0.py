def main():
    P = input().split()
    S = ""
    for i in range(1, 27):
        S += chr(P.index(str(i)) + 97)
    print(S)

if __name__ == '__main__':
    main()