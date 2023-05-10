def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    s = sum(a)
    dic = {}
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in range(q):
        b, c = bc[i]
        if b in dic:
            s += (c - b) * dic[b]
            if c in dic:
                dic[c] += dic[b]
            else:
                dic[c] = dic[b]
            del dic[b]
        print(s)
