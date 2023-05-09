def main():
    P = list(map(int, input().split()))
    S = "abcdefghijklmnopqrstuvwxyz"
    T = [0]*26
    for i in range(26):
        T[P[i]-1] = S[i]
    print("".join(T))

if __name__ == '__main__':
    main()