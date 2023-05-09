def main():
    K = int(input())
    # すぬけ数を格納するリスト
    snuke = []
    # すぬけ数を求めていく
    for i in range(1, 10):
        snuke.append(i)
    for i in range(10, 10**15+1):
        if i % 10 == 0:
            continue
        if i % sum(map(int, str(i))) == 0:
            snuke.append(i)
    # K 番目までのすぬけ数を出力
    for i in range(K):
        print(snuke[i])
