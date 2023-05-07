def main():
    n = int(input())
    r = []
    for i in range(n):
        s, p = input().split()
        r.append((s, -int(p), i+1))
    r.sort()
    for _, _, i in r:
        print(i)
