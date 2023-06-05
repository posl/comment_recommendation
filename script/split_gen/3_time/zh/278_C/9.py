def main():
    n,q = map(int,input().split())
    follow = [set() for _ in range(n)]
    for _ in range(q):
        t,a,b = map(int,input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            follow[a].discard(b)
        elif t == 3:
            print("Yes" if b in follow[a] else "No")
