def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j-i != k-j:
                    ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()