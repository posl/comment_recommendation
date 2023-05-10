def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = [int(x) for x in input().split()]
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    print(max(a[-1], b[-1]))
