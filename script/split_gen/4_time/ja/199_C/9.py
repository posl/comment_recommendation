def main():
    n = int(input())
    s = input()
    q = int(input())
    s = list(s)
    f = 0
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if f == 1:
                if a > n:
                    a -= n
                else:
                    a += n
                if b > n:
                    b -= n
                else:
                    b += n
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            f = 1 - f
    if f == 1:
        s = s[n:] + s[:n]
    print("".join(s))
