def main():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    current = n
    for i in range(m):
        current -= a[i] - b[i-1]
        if current <= 0:
            print("No")
            return
        current = min(n, current + b[i] - a[i])
    current -= t - b[m-1]
    if current <= 0:
        print("No")
        return
    print("Yes")
