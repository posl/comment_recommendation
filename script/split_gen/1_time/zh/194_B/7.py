def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_time = 10 ** 10
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[j]
            else:
                time = max(a[i], b[j])
            if time < min_time:
                min_time = time
    print(min_time)
