def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    # print(n, k, d, a)
    # すぬけ君のリストを作る
    snuke = [0] * n
    for i in range(k):
        for j in range(d[i]):
            snuke[a[i][j] - 1] += 1
    # print(snuke)
    # お菓子を持っていないすぬけ君を数える
    count = 0
    for i in range(n):
        if snuke[i] == 0:
            count += 1
    # print(count)
    print(count)

if __name__ == '__main__':
    main()