def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        S1 = S[:i]
        S2 = S[i:]
        l = 0
        for j in range(i):
            if S1[j] != S2[j]:
                l += 1
        print(l)

if __name__ == '__main__':
    main()