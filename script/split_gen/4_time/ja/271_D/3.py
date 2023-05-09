def main():
    n, s = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ans = []
    for i in range(2**n):
        tmp = []
        for j in range(n):
            if (i >> j) & 1:
                tmp.append(ab[j][1])
            else:
                tmp.append(ab[j][0])
        if sum(tmp) == s:
            ans = tmp
            break
    if ans:
        print("Yes")
        for i in ans:
            print("T" if i == ab[ans.index(i)][1] else "H", end="")
        print()
    else:
        print("No")
