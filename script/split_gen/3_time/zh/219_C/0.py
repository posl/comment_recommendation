def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    d = {c : i for i, c in enumerate(x)}
    s.sort(key=lambda x: [d[c] for c in x])
    print('\n'.join(s))
