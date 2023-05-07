def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort(key=lambda e: [x.index(c) for c in e])
    print(*s, sep='
')
