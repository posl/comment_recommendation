def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                l += 1
            else:
                break
        print(l)

if __name__ == '__main__':
    main()