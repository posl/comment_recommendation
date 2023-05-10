def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    total = []
    for i in range(n):
        for j in range(n):
            if i == j:
                total.append(a[i] + b[j])
            else:
                total.append(max(a[i], b[j]))
    print(min(total))
