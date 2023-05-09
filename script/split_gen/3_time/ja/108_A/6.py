def main():
    K = int(input())
    # K = 3
    # K = 6
    # K = 11
    # K = 50
    # K = 100
    # 偶数と奇数の組み合わせを求める
    # 1. 偶数の個数と奇数の個数を求める
    # 2. それぞれの個数の組み合わせを求める
    # 3. 2の値をかける
    # 1.
    even = 0
    odd = 0
    for i in range(1,K+1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    # 2.
    even_combi = 0
    odd_combi = 0
    for i in range(1,even+1):
        even_combi += i
    for i in range(1,odd+1):
        odd_combi += i
    # 3.
    combi = even_combi * odd_combi
    print(combi)
