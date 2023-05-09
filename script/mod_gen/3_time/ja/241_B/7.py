def main():
    #入力
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #処理
    A.sort()
    B.sort()
    ans = "Yes"
    for b in B:
        if b not in A:
            ans = "No"
            break
    #出力
    print(ans)

if __name__ == '__main__':
    main()