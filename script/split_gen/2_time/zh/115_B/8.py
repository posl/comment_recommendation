def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p[len(p)-1] = p[len(p)-1] / 2
    print(int(sum(p)))
