def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(N):
        b.append(a[i])
        if len(b) >= 2 and b[-2] == b[-1]:
            b.pop()
            b.pop()
        c.append(len(b))
    print("\n".join(map(str, c)))
