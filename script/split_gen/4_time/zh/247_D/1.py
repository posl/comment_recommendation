def main():
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    ans = []
    for i in range(Q):
        if query[i][0] == '1':
            ans.append(query[i][1])
        else:
            ans.pop(0)
    print(sum(list(map(int,ans))))
