def main():
    n, q = map(int, input().split())
    # print(n, q)
    follow = [False] * (n * n)
    # print(follow)
    def follow_check(a, b):
        if a == b:
            return False
        if a > b:
            a, b = b, a
        return follow[a * n + b]
    def follow_set(a, b):
        if a == b:
            return
        if a > b:
            a, b = b, a
        follow[a * n + b] = True
    def follow_unset(a, b):
        if a == b:
            return
        if a > b:
            a, b = b, a
        follow[a * n + b] = False
    for i in range(q):
        t, a, b = map(int, input().split())
        # print(t, a, b)
        if t == 1:
            follow_set(a, b)
        elif t == 2:
            follow_unset(a, b)
        elif t == 3:
            if follow_check(a, b):
                print('Yes')
            else:
                print('No')
