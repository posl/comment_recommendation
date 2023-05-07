def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    ans = []
    # 総和
    total = 0
    # 操作後のリスト
    li = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            c = query[2]
            li += [x] * c
            total += x * c
        else:
            c = query[1]
            ans.append(total)
            total -= sum(li[:c])
            li = li[c:]
    print('
'.join(map(str, ans)))
