def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    c = list(zip(a, b))
    c.sort(key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += c[i][0]
        if t > c[i][1]:
            print("No")
            exit()
    print("Yes")
