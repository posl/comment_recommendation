def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]
    for i in range(n):
        b.append(b[i] + a[i])
    for i in range(n):
        if b[i] <= t <= b[i + 1]:
            print(i + 1, t - b[i])
            break
