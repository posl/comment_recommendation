def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #問題文の通りに実装
    ans1 = 0
    ans2 = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[j] and i == j:
                ans1 += 1
            if A[i] == B[j] and i != j:
                ans2 += 1
    #出力
    print(ans1)
    print(ans2)

if __name__ == '__main__':
    main()