def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    # 1-indexed
    bit = [0] * (n+1)
    def add(i, x):
        while i <= n:
            bit[i] += x
            i += i & (-i)
    def sum(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i & (-i)
        return res
    for i, x in enumerate(a):
        add(i+1, x)
    for query_type, *query_value in query:
        if query_type == 1:
            x = query_value[0]
            for i in range(1, n+1):
                add(i, x)
        elif query_type == 2:
            i, x = query_value
            add(i, x)
        else:
            i = query_value[0]
            print(sum(i))
