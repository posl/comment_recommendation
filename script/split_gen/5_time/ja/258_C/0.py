def main():
    n, q = map(int, input().split())
    s = input()
    queries = [list(map(str, input().split())) for _ in range(q)]
    for query in queries:
        if query[0] == '1':
            s = s[-int(query[1]):] + s[:-int(query[1])]
        else:
            print(s[int(query[1]) - 1])
