def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(q)]
    # indexをキーにして、その数値が何番目かを保存する辞書
    # 例：{1: [0, 4], 2: [2, 5], 3: [3]}
    dic = {}
    for i, v in enumerate(a):
        if v in dic:
            dic[v].append(i)
        else:
            dic[v] = [i]
    for x, k in queries:
        if x in dic and len(dic[x]) >= k:
            print(dic[x][k - 1] + 1)
        else:
            print(-1)

if __name__ == '__main__':
    main()