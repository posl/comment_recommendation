def main():
    n, q = map(int, input().split())
    s = input()
    queries = [input().split() for _ in range(q)]
    #print(n, q, s, queries)
    for query in queries:
        if query[0] == '1':
            s = s[-int(query[1]):] + s[:-int(query[1])]
        else:
            print(s[int(query[1]) - 1])
