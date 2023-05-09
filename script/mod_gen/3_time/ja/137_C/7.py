def main():
    #入力
    N = int(input())
    S = [input() for _ in range(N)]
    #アナグラムの数を数える
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    #出力
    print(ans)

if __name__ == '__main__':
    main()