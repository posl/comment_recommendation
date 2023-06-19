def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        for k in range(i, N):
            if S[k] != S[k-i]:
                l = k
        print(l)

if __name__ == '__main__':
    main()