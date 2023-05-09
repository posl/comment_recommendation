def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = sorted(s, key=lambda s: [x.index(c) for c in s])
    print(*s, sep='\n')
