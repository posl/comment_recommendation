def main():
    n = int(input())
    s = input()
    q = int(input())
    s1 = s[:n]
    s2 = s[n:]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n:
                a -= 1
                b -= 1
                s1 = s1[:a] + s2[b] + s1[a+1:]
                s2 = s2[:b] + s1[a] + s2[b+1:]
            else:
                a -= n
                b -= n
                s2 = s2[:a] + s1[b] + s2[a+1:]
                s1 = s1[:b] + s2[a] + s1[b+1:]
        else:
            s1, s2 = s2, s1
    print(s1 + s2)
