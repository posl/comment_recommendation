def main():
    P = input().split()
    S = ""
    for i in range(1,27):
        S += chr(96 + int(P[i-1]))
    print(S)

if __name__ == '__main__':
    main()