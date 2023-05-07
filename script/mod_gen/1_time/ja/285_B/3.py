def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                l = j+1
            else:
                break
        print(l)
main()

if __name__ == '__main__':
    main()