def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        S1 = S[i:]
        S2 = S[:N-i]
        l = 0
        for j in range(N-i):
            if S1[j] != S2[j]:
                l += 1
            else:
                break
        print(l)

if __name__ == '__main__':
    main()