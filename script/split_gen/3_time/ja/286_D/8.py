def main():
    n, x = map(int, input().split())
    a, b = [], []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    print("Yes" if solve(n, x, a, b) else "No")
