def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #リストAの各要素の出現回数をカウント
    count = [0] * (2 * 10**5 + 1)
    for i in range(N):
        count[A[i]] += 1
    #組み合わせの数を数える
    ans = 0
    for i in range(1, 2 * 10**5 + 1):
        if count[i] >= 2:
            ans += count[i] * (count[i] - 1) // 2
    #出力
    for i in range(N):
        if count[A[i]] >= 2:
            print(ans - count[A[i]] * (count[A[i]] - 1) // 2 + (count[A[i]] - 1) * (count[A[i]] - 2) // 2)
        else:
            print(ans)

if __name__ == '__main__':
    main()