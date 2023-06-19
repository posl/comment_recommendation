def main():
    n, q = map(int, input().split())
    s = input()
    query = []
    for i in range(q):
        query.append(list(map(str, input().split())))
    for i in range(q):
        if query[i][0] == '1':
            s = s[-int(query[i][1]):] + s[:-int(query[i][1])]
        else:
            print(s[int(query[i][1])-1])
