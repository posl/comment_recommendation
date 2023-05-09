def main():
    n, m = map(int, input().split())
    sc = [input().split() for _ in range(m)]
    ans = -1
    for i in range(1000):
        if len(str(i)) == n:
            for s, c in sc:
                if str(i)[int(s) - 1] != c:
                    break
            else:
                ans = i
                break
    print(ans)
