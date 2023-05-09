def main():
    P = input().split()
    S = ""
    for p in P:
        S += chr(96 + int(p))
    print(S)

if __name__ == '__main__':
    main()