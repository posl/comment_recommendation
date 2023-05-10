def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (2*j-i) < N:
                if S[i] != S[j] and S[j] != S[2*j-i] and S[2*j-i] != S[i]:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()