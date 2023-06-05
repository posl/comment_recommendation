def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p[n-1] = p[n-1] // 2
    print(sum(p))
