def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        while l+i < N:
            if S[l] != S[l+i]:
                l += 1
            else:
                break
        print(l)

if __name__ == '__main__':
    main()