def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))
