def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    total = sum(a)
    for query in queries:
        if query[0] == 1:
            total = total + n * query[1]
        elif query[0] == 2:
            total = total - a[query[1] - 1] + query[2]
            a[query[1] - 1] = query[2]
        else:
            print(total)
