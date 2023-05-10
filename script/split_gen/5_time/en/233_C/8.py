def main():
    n, x = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        if i == 0:
            ans = [a for a in l[i]]
        else:
            tmp = []
            for a in l[i]:
                for b in ans:
                    tmp.append(a*b)
            ans = tmp
    print(ans.count(x))
