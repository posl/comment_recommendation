def main():
    n = int(input())
    s = input()
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    for query in queries:
        if query[0] == 1:
            s = s[:query[1]-1] + s[query[2]-1] + s[query[1]:query[2]-1] + s[query[1]-1] + s[query[2]:]
        elif query[0] == 2:
            s = s[n:] + s[:n]
    print(s)
