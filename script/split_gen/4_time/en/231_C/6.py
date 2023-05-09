def main():
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    x = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(n - bisect.bisect_left(a, x[i]))
    print(*ans, sep='\n')
