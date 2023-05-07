def main():
    P = list(map(int, input().split()))
    #print(P)
    S = ""
    for i in range(26):
        S += chr(P[i] + 96)
    print(S)

if __name__ == '__main__':
    main()