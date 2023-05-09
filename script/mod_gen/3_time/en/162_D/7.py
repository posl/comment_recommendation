def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if j-i != k-j:
                    if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()