def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        for j in range(N-i):
            if S[j] != S[i+j]:
                l = j+1
        print(l)

if __name__ == '__main__':
    main()