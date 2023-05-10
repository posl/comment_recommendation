def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    ans = -1
    for i in range(10 ** n):
        si = str(i)
        if len(si) != n:
            continue
        flag = True
        for s, c in sc:
            if si[s - 1] != str(c):
                flag = False
                break
        if flag:
            ans = i
            break
    print(ans)
