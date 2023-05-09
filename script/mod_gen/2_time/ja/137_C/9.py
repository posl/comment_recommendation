def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # ここに処理を書く
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            #print(i,j)
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()