def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort(key=lambda x: [x.index(c) for c in x if c in x])
    for i in range(n):
        print(s[i])
