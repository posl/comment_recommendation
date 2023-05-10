def main():
    n = int(input())
    s = set()
    for i in range(n):
        l = list(map(int, input().split()))
        s.add(tuple(l[1:]))
    print(len(s))
