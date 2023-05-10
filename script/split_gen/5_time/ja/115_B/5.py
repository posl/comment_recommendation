def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort(reverse=True)
    print(sum(p)-p[0]//2)
