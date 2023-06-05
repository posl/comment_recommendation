def main():
    q = int(input())
    a = [0] * q
    b = [0] * q
    for i in range(q):
        a[i], b[i] = map(int, input().split())
    s = []
    for i in range(q):
        if a[i] == 1:
            s.append(b[i])
        else:
            ans = 0
            for j in range(b[i]):
                ans += s[j]
            print(ans)
            s = s[b[i]:]
