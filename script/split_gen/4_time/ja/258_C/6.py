def main():
    n, q = map(int, input().split())
    s = input()
    query = [input().split() for _ in range(q)]
    s = list(s)
    for i in range(q):
        if query[i][0] == "1":
            s[int(query[i][1])-1], s[int(query[i][1])] = s[int(query[i][1])], s[int(query[i][1])-1]
        else:
            print(s[int(query[i][1])-1])
