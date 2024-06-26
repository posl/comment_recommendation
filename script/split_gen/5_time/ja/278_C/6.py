def main():
    N, Q = map(int, input().split())
    follow = [set() for i in range(N)]
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1].add(b-1)
        elif t == 2:
            follow[a-1].discard(b-1)
        else:
            if b-1 in follow[a-1] and a-1 in follow[b-1]:
                print("Yes")
            else:
                print("No")
    return
