def main():
    N = int(input())
    A = list(map(int, input().split()))
    # mod200の値をとるときのindexを保持するリスト
    mod200 = [[] for _ in range(200)]
    # それぞれのmod200の値に対して、indexをmod200のリストに追加する
    for i, a in enumerate(A):
        mod200[a % 200].append(i + 1)
    # mod200の値が2以上ある場合、そのindexの組み合わせを出力する
    for m in mod200:
        if len(m) >= 2:
            print('Yes')
            print(1, m[0])
            print(1, m[1])
            return
    # mod200の値が2以上ない場合、mod200の値をとるときのindexを保持するリスト
    mod200 = [[] for _ in range(200)]
    # それぞれのmod200の値に対して、indexをmod200のリストに追加する
    for i, a in enumerate(A):
        mod200[a % 200].append(i + 1)
    # mod200の値が2以上ある場合、そのindexの組み合わせを出力する
    for m in mod200:
        if len(m) >= 2:
            print('Yes')
            print(1, m[0])
            print(1, m[1])
            return
    # mod200の値が2以上ない場合、Noを出力する
    print('No')
