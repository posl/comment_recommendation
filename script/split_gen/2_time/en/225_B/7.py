def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if a[0] == b[0] and a[-1] == b[-1]:
        print("Yes")
    else:
        print("No")
