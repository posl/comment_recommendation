def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    for _ in range(m):
        u, v = map(int, input().split())
        if abs(u - v) != 1:
            print("No")
            return
    print("Yes")
