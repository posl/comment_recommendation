def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    ans = -1
    for i in range(10 ** n):
        i = str(i)
        if len(i) == n:
            for s, c in sc:
                if i[s - 1] != str(c):
                    break
            else:
                ans = i
                break
    print(ans)
