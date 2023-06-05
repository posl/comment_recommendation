def minTime(n, a, b, c, d, e):
    time = 0
    time += (n + a - 1) // a
    time += (n + b - 1) // b
    time += (n + c - 1) // c
    time += (n + d - 1) // d
    time += (n + e - 1) // e
    return time + 4
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(minTime(n, a, b, c, d, e))
