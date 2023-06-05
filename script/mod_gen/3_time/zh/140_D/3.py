def main():
    N,K = map(int, input().split())
    S = input()
    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
    ans = min(N-1, count+2*K)
    print(ans)

if __name__ == '__main__':
    main()