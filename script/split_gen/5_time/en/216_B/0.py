def main():
    n = int(input())
    names = set()
    for i in range(n):
        s, t = input().split()
        if (s, t) in names:
            print('Yes')
            return
        names.add((s, t))
    print('No')
