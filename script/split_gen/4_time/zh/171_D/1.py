def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    dic = {}
    for a in A:
        dic[a] = dic.get(a, 0) + 1
    ans = sum(A)
    for b, c in BC:
        if b in dic:
            ans += (c - b) * dic[b]
            dic[c] = dic.get(c, 0) + dic[b]
            dic[b] = 0
        print(ans)
