def main():
    P = list(map(int, input().split()))
    S = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(P)):
        print(S[P[i]-1], end = "")
    print("")

if __name__ == '__main__':
    main()