def main():
    n = int(input())
    s_p = []
    for i in range(n):
        s, p = input().split()
        p = int(p)
        s_p.append((s, p, i+1))
    s_p.sort(key=lambda x: (x[0], -x[1]))
    for s, p, i in s_p:
        print(i)
