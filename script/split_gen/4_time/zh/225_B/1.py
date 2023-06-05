def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if a[0] == 1 and b.count(1) == N-1:
        print('Yes')
    else:
        print('No')
