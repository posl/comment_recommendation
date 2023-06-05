def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if S[i] != S[j] and S[j] != S[k] and S[i] != S[k] and j - i != k - j:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()