def main():
    n = int(input())
    s_t = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in s_t:
            s_t[s] = t
        else:
            s_t[s] += t
    s_t = sorted(s_t.items(), key=lambda x: x[1], reverse=True)
    print(s_t[0][0])
