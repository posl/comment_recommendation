def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            k = j + j - i
            if k >= N:
                break
            if S[i] != S[j] and S[i

if __name__ == '__main__':
    main()