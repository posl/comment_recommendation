def main():
    N, M = map(int, input().split())
    ans = 0
    pen = 0
    p = [0] * N
    s = [0] * N
    for i in range(M):
        p[i], s[i] = input().split()
        p[i] = int(p[i])
        if s[i] == "AC":
            if p[i] not in p:
                ans += 1
            else:
                pen += 1
        else:
            if p[i] not in p:
                pen += 1
    print(ans, pen)
    return 0
