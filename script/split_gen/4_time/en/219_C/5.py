def main():
    x = input()
    n = int(input())
    s = [input() for i in range(n)]
    d = dict(zip(x, range(26)))
    s.sort(key=lambda x: [d[c] for c in x])
    print(*s, sep="\n")
