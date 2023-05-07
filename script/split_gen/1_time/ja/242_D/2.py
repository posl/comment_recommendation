def main():
    s = input()
    q = int(input())
    tki = []
    for _ in range(q):
        t, k = map(int, input().split())
        tki.append([t, k])
    for t, k in tki:
        print(solve(s, t, k))
