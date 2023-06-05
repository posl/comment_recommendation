def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [i - 1 for i in p]
    ans = -10 ** 18
    for i in range(n):
        x = i
        s = 0
        l = 0
        while True:
            x = p[x]
            s += c[x]
            l += 1
            if x == i:
                break
        t = 0
        x = i
        while True:
            x = p[x]
            t += c[x]
            l -= 1
            if l == k:
                break
        if s > 0:
            if t > 0:
                u = (k // l - 1) * l
                for j in range(l):
                    x = p[x]
                    t += c[x]
                    if t > ans:
                        ans = t
                for j in range(l):
                    x = p[x]
                    t += c[x]
                    u += 1
                    if t > ans:
                        ans = t
                    if u == k:
                        break
            else:
                for j in range(k):
                    x = p[x]
                    t += c[x]
                    if t > ans:
                        ans = t
        else:
            for j in range(k):
                x = p[x]
                t += c[x]
                if t > ans:
                    ans = t
    print(ans)
