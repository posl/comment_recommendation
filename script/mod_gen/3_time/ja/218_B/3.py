def main():
    P = list(map(int, input().split()))
    S = ""
    for i in range(26):
        S += chr(97 + P[i] - 1)
    print(S)

if __name__ == '__main__':
    main()