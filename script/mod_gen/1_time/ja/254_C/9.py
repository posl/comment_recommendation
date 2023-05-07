def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # Kの倍数になるように並び替える
    A.sort()
    # Kの倍数のところで分割して、それぞれで昇順になっているかを確認する
    # 昇順に並んでいなければNo
    for i in range(0, N, K):
        if A[i:i+K] != sorted(A[i:i+K]):
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()