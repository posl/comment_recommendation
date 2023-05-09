def main():
    n, q = map(int, input().split())
    s = input()
    queries = [list(map(int, input().split())) for _ in range(q)]
    s = list(s)
    for i in range(q):
        if queries[i][0] == 1:
            s.insert(0, s.pop())
        else:
            print(s[queries[i][1]-1])
    return
