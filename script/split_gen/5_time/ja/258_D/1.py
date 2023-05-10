def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = [0] + a
    b = [0] + b
    time = [0] * (n + 1)
    time[1] = a[1] + b[1]
    for i in range(2, n + 1):
        time[i] = min(time[i - 1] + a[i], time[i - 1] + b[i])
    print(time[n] * x)
