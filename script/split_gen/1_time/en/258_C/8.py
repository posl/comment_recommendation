def main():
    # input
    n, q = map(int, input().split())
    s = list(input())
    queries = [list(map(int, input().split())) for _ in range(q)]
    # compute
    for t, x in queries:
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])
