def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    max_a = max(a)
    max_b = max(b)
    if max_a + max_b > 10**9:
        max_day = 10**9
    else:
        max_day = max_a + max_b
    day = [0 for i in range(max_day + 1)]
    for i in range(n):
        for j in range(a[i], a[i] + b[i]):
            day[j] += 1
    for i in range(1, n + 1):
        print(day.count(i), end = " ")
