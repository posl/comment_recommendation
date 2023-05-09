def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j]:
                ans = 1
    if ans == 0:
        print(N)
    else:
        print(N-1)

if __name__ == '__main__':
    main()