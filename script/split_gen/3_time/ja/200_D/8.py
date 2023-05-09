def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 200 で割った余りをキーにして、その値が 2 以上のときに答えとなる
    d = {}
    for i, x in enumerate(a):
        x %= 200
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    # 答えがない場合
    if not any([d[x] >= 2 for x in d]):
        print('No')
        return
    # 答えがある場合
    print('Yes')
    # 2 つ以上ある余りのうち、最初に見つかったものを出力
    for i, x in enumerate(a):
        x %= 200
        if d[x] >= 2:
            print(i + 1, end=' ')
            d[x] -= 1
            if d[x] == 0:
                del d[x]
        if not d:
            break
    print()
    # 2 つ以上ある余りのうち、次に見つかったものを出力
    for i, x in enumerate(a):
        x %= 200
        if x in d:
            print(i + 1, end=' ')
            d[x] -= 1
            if d[x] == 0:
                del d[x]
        if not d:
            break
    print()
