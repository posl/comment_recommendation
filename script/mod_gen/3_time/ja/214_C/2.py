def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = []
    for i in range(N):
        ans.append(T[i])
        for j in range(i+1, i+N):
            if ans[i] > T[j%N]:
                ans[i] = T[j%N]
            else:
                ans[i] += S[j%N]
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()