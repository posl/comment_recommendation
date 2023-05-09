def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの中で最も多く出現する数字を求める
    num = [0] * 200001
    for i in range(N):
        num[A[i]] += 1
    max_num = max(num)
    # print(max_num)
    # Aの中で最も多く出現する数字の個数を求める
    max_num_count = 0
    for i in range(200001):
        if num[i] == max_num:
            max_num_count += 1
    # print(max_num_count)
    # Aの中で最も多く出現する数字の個数をNから引いた数が答え
    print(N - max_num_count)

if __name__ == '__main__':
    main()