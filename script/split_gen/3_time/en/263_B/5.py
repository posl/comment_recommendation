def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    g = 0
    for i in range(n, 0, -1):
        if p[i] == 1:
            g += 1
            break
        else:
            g += 1
            i = p[i]
    print(g)
