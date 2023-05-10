def main():
    a, b, c, d, e = map(int, input().split())
    ans = len(set([a, b, c, d, e]))
    print(ans)
