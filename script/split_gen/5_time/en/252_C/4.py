def main():
    n = int(input())
    s = [input() for _ in range(n)]
    l = 0
    for i in range(n):
        l = max(l, len(set(s[i])))
    print(l)
